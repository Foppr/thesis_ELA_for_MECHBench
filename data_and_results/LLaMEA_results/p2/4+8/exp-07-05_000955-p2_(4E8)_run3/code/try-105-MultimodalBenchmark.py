import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global convergence
        f1 = np.sum(x**2)
        
        # Chaotic sine-wave interactions with varying frequencies and amplitudes
        f2 = 0.5 * np.sum(np.sin(10.0 * x) * np.cos(7.0 * x) * np.sin(3.0 * x))
        
        # Radial basis function with dynamic conditioning and Gaussian modulation
        f3 = 0.3 * np.sum(np.exp(-0.5 * np.sum(x**2)) * np.sin(5.0 * np.sum(x**2)))
        
        # Asymmetric polynomial coupling with cross-terms
        f4 = 0.2 * np.sum(x**3 * np.sin(4.0 * x) + x**5 * np.cos(3.0 * x))
        
        # Multi-scale trigonometric modulation with adaptive frequency
        f5 = 0.25 * np.sum(np.sin(15.0 * x) * np.cos(12.0 * x) * np.sin(9.0 * x))
        
        # Nonlinear interaction with exponential decay and polynomial scaling
        f6 = 0.15 * np.sum(np.exp(-0.2 * np.sum(x**2)) * x**4 * np.sin(6.0 * x))
        
        # Coupled sine and cosine waves with variable phase shifts
        f7 = 0.1 * np.sum(np.sin(8.0 * x + np.cos(5.0 * x)) * np.cos(6.0 * x + np.sin(4.0 * x)))
        
        # Enhanced multimodal structure using nested trigonometric functions
        f8 = 0.12 * np.sum(np.sin(20.0 * x) * np.cos(15.0 * x) * np.sin(10.0 * x))
        
        # Polynomial coupling with dynamic weights and sine modulation
        f9 = 0.08 * np.sum((x**4) * np.sin(5.0 * x) * np.cos(7.0 * x))
        
        # Asymmetric Gaussian interaction term with varying centers
        f10 = 0.09 * np.sum(np.exp(-0.3 * ((x - 1.0)**2 + (x + 1.0)**2)) * np.sin(12.0 * x))
        
        # Combined non-separable structure with chaotic modulation
        f11 = 0.1 * np.sum(np.sin(18.0 * x) * np.cos(14.0 * x) * np.exp(-0.1 * np.sum(x**2)) * x**3)
        
        # Final term with complex interaction and high-frequency oscillation
        f12 = 0.07 * np.sum(np.sin(25.0 * x) * np.cos(20.0 * x) * np.sin(15.0 * x) * np.exp(-0.05 * np.sum(x**2)))
        
        # Combine all terms
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12