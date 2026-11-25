import numpy as np

class FractalRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Fractal Brownian motion parameters
        self.hurst = np.random.uniform(0.1, 0.9, dim)
        self.fractal_amplitudes = np.random.uniform(0.5, 2.0, dim)
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, 10))
        self.rbf_widths = np.random.uniform(0.5, 3.0, 10)
        # Trigonometric coupling coefficients
        self.trig_amplitudes = np.random.uniform(0.1, 1.0, dim)
        self.trig_frequencies = np.random.randint(1, 6, dim)
        # Additional chaotic parameter for enhanced irregularity
        self.noise_weights = np.random.uniform(0.5, 1.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal Brownian motion component
        fbm_sum = 0
        for i in range(self.dim):
            # Simplified fractal Brownian motion approximation
            xi = x[i]
            fbm_term = 0
            for k in range(1, 6):  # Sum first 5 harmonics
                fbm_term += (1.0 / (k**self.hurst[i])) * np.sin(k * xi)
            fbm_sum += fbm_term * self.fractal_amplitudes[i]
        
        # Radial basis function component
        rbf_sum = 0
        for i in range(self.dim):
            rbf_term = 0
            for j in range(10):
                center = self.rbf_centers[i, j]
                width = self.rbf_widths[j]
                rbf_term += np.exp(-0.5 * ((x[i] - center) / width)**2)
            rbf_sum += rbf_term
        
        # Trigonometric coupling component
        trig_sum = 0
        for i in range(self.dim):
            xi = x[i]
            trig_term = (self.trig_amplitudes[i] * 
                        np.sin(self.trig_frequencies[i] * xi) + 
                        self.trig_amplitudes[i] * 
                        np.cos(self.trig_frequencies[i] * xi))
            trig_sum += trig_term
        
        # Combine all components with adjusted weights
        result = (0.8 * fbm_sum + 
                 1.2 * rbf_sum + 
                 0.6 * trig_sum)
        
        return result