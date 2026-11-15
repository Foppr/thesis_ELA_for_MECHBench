import numpy as np

class HybridAdaptiveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute frequency components for efficiency
        self.freqs = np.arange(1, dim + 1)
        self.coeffs = np.random.uniform(0.5, 2.0, dim)
    
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Polynomial term with adaptive coefficients
        poly = np.sum(self.coeffs * np.abs(x_norm)**(1.5 + np.abs(x_norm)))
        
        # Trigonometric mixture with varying amplitudes
        trig = np.sum(np.sin(self.freqs * x_norm) * np.cos(self.freqs * x_norm * 1.3) * 
                     (1.0 + 0.3 * np.sin(0.5 * self.freqs)))
        
        # Radial basis function component with dynamic centers
        centers = np.linspace(-1, 1, self.dim)
        rbf = 0.0
        for i in range(self.dim):
            dist = np.sum((x_norm - centers[i])**2)
            rbf += np.exp(-dist * (1.0 + 0.2 * np.sin(i)))
        
        # Asymmetric global optimum with multiple local minima
        asym = np.sum((x_norm - 0.3)**4 + (x_norm + 0.2)**3)
        
        # Coupled oscillatory terms with frequency modulation
        coupled = 0.0
        for i in range(self.dim - 1):
            coupled += np.sin(2 * (x_norm[i] + x_norm[i+1])) * np.cos(3 * (x_norm[i] - x_norm[i+1]))
        
        # Adaptive conditioning based on dimensionality
        cond = np.sum(np.abs(x_norm)**(1.0 + 0.1 * self.dim))
        
        # Final hybrid combination
        return 1.2 * poly + 0.8 * trig + 0.5 * rbf + 1.5 * asym + 0.7 * coupled + 0.3 * cond