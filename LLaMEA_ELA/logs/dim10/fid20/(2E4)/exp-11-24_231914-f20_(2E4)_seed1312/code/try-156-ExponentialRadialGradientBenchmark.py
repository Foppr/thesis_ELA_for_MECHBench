import numpy as np

class ExponentialRadialGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Exponential decay parameters for potential wells
        self.decay_rates = np.random.uniform(0.5, 2.0, size=dim)
        self.well_depths = np.random.uniform(1.0, 5.0, size=dim)
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-4.0, 4.0, size=(dim, 3))
        self.rbf_widths = np.random.uniform(0.5, 2.0, size=3)
        # Adaptive gradient field parameters
        self.gradient_magnitudes = np.random.uniform(0.1, 1.0, size=dim)
        self.gradient_angles = np.random.uniform(0, 2*np.pi, size=dim)
        # Saddle point configuration
        self.saddle_points = np.random.uniform(-3.0, 3.0, size=(2, dim))
        self.saddle_strengths = np.random.uniform(0.5, 2.0, size=2)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay potential wells
        exp_potential = 0.0
        for i in range(self.dim):
            rate = self.decay_rates[i]
            depth = self.well_depths[i]
            exp_potential += depth * np.exp(-rate * np.abs(x[i]))
            
        # Radial basis function coupling
        rbf_coupling = 0.0
        for i in range(self.dim):
            for j in range(3):
                center = self.rbf_centers[i, j]
                width = self.rbf_widths[j]
                rbf_coupling += np.exp(-0.5 * ((x[i] - center) / width)**2)
                
        # Adaptive gradient field component
        grad_field = 0.0
        for i in range(self.dim):
            mag = self.gradient_magnitudes[i]
            angle = self.gradient_angles[i]
            grad_field += mag * np.sin(angle + x[i]) * np.cos(angle + x[i])
            
        # Saddle point structures
        saddle_contrib = 0.0
        for k in range(2):
            strength = self.saddle_strengths[k]
            saddle_point = self.saddle_points[k]
            dist = np.sum((x - saddle_point)**2)
            saddle_contrib += strength * np.exp(-dist / 10.0) * np.cos(dist / 5.0)
            
        # Base conditioning term
        base_conditioning = np.sum(x**2) / self.dim
        
        # Dynamic complexity factor based on dimension
        complexity_factor = 1.0 + 0.05 * np.log(self.dim + 1)
        
        # Final objective function
        result = complexity_factor * (exp_potential + rbf_coupling + grad_field + 
                                    saddle_contrib + base_conditioning)
        
        return result