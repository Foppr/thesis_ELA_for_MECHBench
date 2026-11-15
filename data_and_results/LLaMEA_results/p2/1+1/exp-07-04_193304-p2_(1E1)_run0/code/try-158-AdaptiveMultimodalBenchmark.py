import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Polynomial terms with varying degrees and adaptive coefficients
        f1 = np.sum(x_norm**2)
        f2 = 0.3 * np.sum(x_norm**3)
        f3 = 0.15 * np.sum(x_norm**4)
        
        # Trigonometric components with adaptive frequencies
        freqs = np.arange(1, self.dim + 1) * (2.0 + 0.5 * np.sin(np.arange(self.dim) * 0.3))
        f4 = np.sum(np.sin(freqs * x_norm) * np.cos(freqs * x_norm))
        f5 = np.sum(np.sin(freqs * x_norm**2))
        
        # Radial basis function component with adaptive widths
        widths = 0.5 + 0.5 * np.sin(np.arange(self.dim) * 0.4)
        rb = np.sum(np.exp(-0.5 * np.sum(((x_norm[:, np.newaxis] - np.arange(self.dim)) / widths)**2, axis=0)))
        f6 = 0.25 * rb
        
        # Asymmetric penalty terms
        f7 = 0.3 * np.sum(np.where(x_norm > 0, x_norm**2.5, x_norm**1.5))
        f8 = 0.2 * np.sum(np.where(x_norm < 0, np.abs(x_norm)**3, np.abs(x_norm)**2))
        
        # Cross-dimensional coupling with varying strengths
        coupling_strengths = 0.1 + 0.3 * np.sin(np.arange(self.dim-1) * 0.5)
        f9 = np.sum(coupling_strengths * np.sin(x_norm[:-1]) * np.cos(x_norm[1:]))
        
        # Adaptive dimensionality scaling
        dim_scaling = 1.0 + 0.2 * np.sin(np.arange(self.dim) * 0.7)
        f10 = 0.15 * np.sum(x_norm**2 * dim_scaling)
        
        # Multi-scale oscillation with dynamic amplitude
        amp = 1.0 + 0.5 * np.sin(np.arange(self.dim) * 0.8)
        f11 = 0.2 * np.sum(amp * np.sin(10 * x_norm) * np.exp(-0.1 * np.abs(x_norm)))
        
        # Fractional power interactions
        f12 = 0.1 * np.sum(np.abs(x_norm)**(1.3 + 0.4 * np.sin(np.arange(self.dim) * 0.6)))
        
        # Hyperbolic tangent based interactions
        f13 = 0.18 * np.sum(np.tanh(x_norm * np.sin(x_norm * 0.5)))
        
        # Conditional exponential terms
        f14 = 0.22 * np.sum(np.exp(-0.5 * np.abs(x_norm)) * np.sin(5 * x_norm))
        
        # Adaptive coupling with sine modulation
        f15 = 0.12 * np.sum(np.sin(x_norm[:-1] * x_norm[1:]) * np.cos(x_norm[:-1] * x_norm[1:] * 0.3))
        
        # Combined penalty with logarithmic scaling
        f16 = 0.14 * np.sum(np.log(1.1 + np.abs(x_norm)) * x_norm**2)
        
        # Fractional dimensionality effect with cosine modulation
        f17 = 0.08 * np.sum(np.abs(x_norm)**(1.2 + 0.3 * np.cos(np.arange(self.dim) * 0.4)))
        
        # Multi-modal sine with varying frequency and amplitude
        f18 = 0.25 * np.sum(np.sin(8 * x_norm + np.sin(4 * x_norm)) * np.exp(-0.3 * x_norm**2))
        
        # Adaptive scaling with exponential decay
        f19 = 0.16 * np.sum(np.exp(-0.3 * np.abs(x_norm)) * np.sin(12 * x_norm))
        
        # Cross-dimensional interaction with polynomial coupling
        f20 = 0.1 * np.sum((x_norm[:-1]**2 + x_norm[1:]**2) * np.sin(x_norm[:-1] * x_norm[1:]))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15 + f16 + f17 + f18 + f19 + f20