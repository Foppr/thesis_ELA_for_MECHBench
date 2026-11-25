import numpy as np

class PolynomialGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial potential terms with varying degrees
        poly_term = np.sum(x_scaled**4) + 0.5 * np.sum(x_scaled**6)
        
        # Gaussian hill components centered at multiple locations
        gaussian_term = 0.0
        centers = np.linspace(-0.8, 0.8, min(5, self.dim))
        for i in range(len(centers)):
            if i < self.dim:
                gaussian_term += np.exp(-10.0 * (x_scaled[i] - centers[i])**2)
        
        # Trigonometric coupling between dimensions with frequency modulation
        trig_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 1.0 + 0.5 * np.sin(x_scaled[i])
                freq_j = 1.0 + 0.3 * np.cos(x_scaled[j])
                trig_coupling += np.sin(freq_i * x_scaled[i] + freq_j * x_scaled[j]) * \
                                np.cos(0.5 * x_scaled[i] - 0.7 * x_scaled[j])
        
        # Mixed harmonic and exponential decay component
        mixed_term = 0.0
        for i in range(self.dim):
            mixed_term += (np.sin(3.0 * x_scaled[i]) * np.exp(-0.5 * x_scaled[i]**2) + 
                          0.3 * np.cos(4.0 * x_scaled[i]) * np.exp(-0.3 * x_scaled[i]**2))
        
        # Radial polynomial with sinusoidal modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial_poly = r**3 * (1.0 + 0.2 * np.sin(5.0 * r))
        
        # Combine all terms with different weights
        return 1.2 * poly_term + 0.9 * gaussian_term + 0.7 * trig_coupling + \
               0.6 * mixed_term + 0.8 * radial_poly + 3.1