import numpy as np

class GaussianTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian radial basis components with varying widths and centers
        gaussians = 0.0
        centers = np.linspace(-4.5, 4.5, 9)
        widths = np.logspace(-1, 1, 9)
        for i, (c, w) in enumerate(zip(centers, widths)):
            gaussians += np.exp(-w * np.sum((x - c)**2)) * np.sin(i * np.pi * x / 5.0)
        
        # Trigonometric polynomial interactions with varying frequencies and amplitudes
        trig_poly = np.sum(np.sin(1.5 * x) * np.cos(2.0 * x) + 
                          0.5 * np.sin(3.0 * x) * np.cos(4.0 * x) + 
                          0.3 * np.sin(5.0 * x) * np.cos(6.0 * x))
        
        # Adaptive gradient modulation with exponential decay
        grad_mod = np.sum(np.exp(-0.1 * np.abs(x)) * (x**2 + 0.1 * x**4) * 
                         np.sin(0.5 * x) * np.cos(0.3 * x))
        
        # Multi-scale sine-wave interference patterns
        interference = np.sum(np.sin(2.0 * x) * np.cos(3.0 * x) * 
                            np.sin(4.0 * x) * np.cos(5.0 * x))
        
        # Polynomial coupling with sinusoidal modulation
        poly_coupling = np.sum(0.2 * x**3 * np.sin(0.8 * x) + 
                             0.1 * x**5 * np.cos(0.6 * x) + 
                             0.05 * x**7 * np.sin(0.4 * x))
        
        # Asymmetric penalty terms with exponential weighting
        asym_penalty = np.sum(np.exp(0.5 * x) * (x > 0) + np.exp(-0.5 * x) * (x <= 0))
        
        # Global conditioning factor with fractal-like scaling
        condition_factor = 0.01 * np.sum(x**2 * (1 + 0.1 * np.sin(10.0 * x)))
        
        return gaussians + trig_poly + grad_mod + interference + poly_coupling + asym_penalty + condition_factor