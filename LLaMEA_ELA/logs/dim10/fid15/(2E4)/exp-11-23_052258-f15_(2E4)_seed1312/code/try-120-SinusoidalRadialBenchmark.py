import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis parameters
        self.radial_centers = np.random.uniform(-4.0, 4.0, (dim, 3))
        self.radial_widths = np.random.uniform(0.5, 2.0, (dim, 3))
        self.frequency_modulators = np.random.uniform(0.5, 2.0, dim)
        self.conditioning_factors = np.random.uniform(0.1, 10.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with sinusoidal modulation
        radial_term = 0.0
        for i in range(self.dim):
            center = self.radial_centers[i]
            width = self.radial_widths[i]
            for j in range(3):
                dist = np.sum((x - center[j])**2)
                radial_term += np.exp(-dist / (2 * width[j]**2)) * np.sin(2 * np.pi * x[i] * self.frequency_modulators[i])
                
        # Cross-dimensional coupling with harmonic interactions
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling_term += np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Dynamic conditioning with time-varying weights
        conditioning_term = 0.0
        for i in range(self.dim):
            condition_factor = self.conditioning_factors[i]
            conditioning_term += condition_factor * (np.sin(x[i])**2 + np.cos(x[i])**2)
            
        # Multi-scale oscillatory landscape with varying amplitudes
        oscillation_term = 0.0
        amplitudes = [1.0, 0.5, 0.25, 0.125]
        for i in range(self.dim):
            for amp in amplitudes:
                oscillation_term += amp * np.sin(amp * x[i]) * np.cos(amp * x[i])
                
        # Asymmetric potential wells with varying depths and widths
        well_term = 0.0
        for i in range(self.dim):
            # Asymmetric well with dynamic parameters
            depth = 1.0 + 0.5 * np.sin(0.5 * i)
            width = 0.5 + 0.3 * np.cos(0.3 * i)
            asymmetry = 0.2 * np.sin(0.7 * i)
            well_term += depth * (np.exp(-((x[i] - asymmetry)**2) / (2 * width**2)) - 0.5)
            
        # Combine all terms with carefully balanced weights
        weights = [0.22, 0.18, 0.20, 0.25, 0.15]
        total = (weights[0] * radial_term + 
                weights[1] * coupling_term + 
                weights[2] * conditioning_term + 
                weights[3] * oscillation_term + 
                weights[4] * well_term)
                
        # Add dimensionality-based scaling with sinusoidal adjustment
        scale = 1.0 + 0.2 * np.sin(self.dim * 0.3) + 0.1 * np.sum(np.abs(x)**1.2)
        
        return scale * total