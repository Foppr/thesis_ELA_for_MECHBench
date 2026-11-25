import numpy as np

class HelicalGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Helical spiral arrangement of Gaussian peaks
        f1 = 0.0
        num_peaks = min(10, self.dim)
        
        for i in range(num_peaks):
            # Create helical pattern in the coordinate space
            angle = 2 * np.pi * i / num_peaks
            radius = 0.5 + 0.3 * np.sin(angle)
            
            # Peak center in normalized space
            center_x = radius * np.cos(angle)
            center_y = radius * np.sin(angle)
            
            # Gaussian peak contribution
            peak_val = np.exp(-0.5 * ((x_norm[0] - center_x)**2 + (x_norm[1] - center_y)**2) / 0.1**2)
            f1 += peak_val
            
        # Adaptive noise term based on dimensionality
        noise_amp = 0.1 / (1.0 + self.dim / 10.0)
        noise = noise_amp * np.random.random()
        
        # Dimensionality-dependent conditioning
        cond_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        
        # Cross-dimensional interaction terms
        f2 = 0.0
        for i in range(self.dim - 1):
            f2 += (x_norm[i] - x_norm[i+1])**2 * np.cos(3 * x_norm[i])
            
        # Exponentially decaying harmonic terms
        f3 = 0.0
        for i in range(self.dim):
            freq = 2**(i % 3 + 1)
            f3 += np.sin(freq * x_norm[i]) * np.exp(-0.1 * i)
            
        # Asymmetric basin shaping
        f4 = 0.0
        for i in range(self.dim):
            f4 += (x_norm[i]**3) * np.exp(-0.5 * x_norm[i]**2)
            
        # Return combined function value
        return cond_factor * (f1 + f2 + f3 + f4) + noise