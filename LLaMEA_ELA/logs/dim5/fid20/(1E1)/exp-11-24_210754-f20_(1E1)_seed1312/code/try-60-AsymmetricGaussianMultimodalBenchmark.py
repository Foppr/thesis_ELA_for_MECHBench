import numpy as np

class AsymmetricGaussianMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic conditioning term
        f1 = np.sum(x**2) / self.dim
        
        # Asymmetric Gaussian peaks with varying heights and widths
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Asymmetric peak: one side steeper than the other
            peak_height = 10.0 * (1.0 + 0.3 * np.sin(i * 0.7))
            width = 1.5 + 0.5 * np.cos(i * 0.9)
            # Asymmetric Gaussian: different decay on left vs right
            gaussian = peak_height * np.exp(-0.5 * ((xi - 2.0) / width)**2) + \
                       0.5 * peak_height * np.exp(-0.5 * ((xi + 2.0) / (width * 0.6))**2)
            f2 += gaussian
        
        # Periodic trigonometric modulations with varying frequencies
        f3 = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq = 10.0 + 5.0 * np.sin(i * 0.6)
            f3 += np.sin(freq * xi) * np.cos(freq * xi**1.5)
        
        # Cross-dimensional interaction terms with asymmetric coupling
        f4 = 0.0
        for i in range(self.dim - 1):
            xi, xip1 = x[i], x[i+1]
            # Asymmetric interaction: stronger influence from xi on xip1
            interaction = 2.0 * np.sin(xi) * np.cos(1.5 * xip1) + \
                          0.8 * np.cos(xi) * np.sin(1.2 * xip1)
            f4 += interaction
        
        # Add noise-like perturbations with chaotic scaling
        f5 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Chaotic modulation using sine and cosine with varying phases
            phase = 3.0 * np.sin(i * 1.1) + 2.0 * np.cos(i * 0.8)
            noise = np.sin(7.0 * xi + phase) * np.cos(5.0 * xi**2 + phase)
            f5 += noise**2
        
        # Polynomial corruption with fractional exponents
        f6 = 0.05 * np.sum((x**3.2 + 0.8 * x**2.4 + 0.5 * x**1.9) / self.dim)
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + f6