import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Base polynomial terms with varying exponents
        f1 = np.sum(x_norm**2)
        f2 = 0.5 * np.sum(x_norm**3)
        f3 = 0.3 * np.sum(x_norm**4)
        f4 = 0.2 * np.sum(x_norm**5)
        
        # Sinusoidal components with non-uniform frequencies
        freqs = np.arange(1, self.dim + 1) * np.pi
        f5 = np.sum(np.sin(freqs * x_norm))
        f6 = np.sum(np.cos(freqs * x_norm))
        
        # Chaotic interaction using sine and cosine combinations
        f7 = np.sum(np.sin(x_norm * np.sin(x_norm)))
        f8 = np.sum(np.cos(x_norm * np.cos(x_norm)))
        
        # Exponential decay with varying rates
        rates = np.arange(1, self.dim + 1) * 0.2
        f9 = np.sum(np.exp(-rates * np.abs(x_norm)))
        
        # Cross-dimensional interactions with non-linear coupling
        f10 = 0.1 * np.sum(np.sin(x_norm[:-1] * x_norm[1:]))
        f11 = 0.1 * np.sum(np.cos(x_norm[:-1] * x_norm[1:]))
        
        # High-frequency oscillation with amplitude modulation
        f12 = np.sum(np.sin(20 * x_norm) * np.exp(-0.5 * x_norm**2))
        
        # Power-law interaction with varying exponents
        f13 = 0.05 * np.sum(np.abs(x_norm)**(3.5 + np.sin(np.arange(self.dim)) * 2))
        
        # Additional chaotic sine-cosine interaction
        f14 = 0.2 * np.sum(np.sin(15 * x_norm) * np.cos(12 * x_norm))
        
        # Modified exponential term with logarithmic scaling
        f15 = 0.15 * np.sum(np.exp(-np.abs(x_norm) * np.log(1 + np.abs(x_norm))))
        
        # Combined polynomial and trigonometric term
        f16 = 0.1 * np.sum((x_norm**2 + np.sin(x_norm))**2)
        
        # Fractional power term for added complexity
        f17 = 0.08 * np.sum(np.abs(x_norm)**1.7)
        
        # Non-uniform frequency sine term
        f18 = 0.25 * np.sum(np.sin(25 * x_norm * (1 + 0.1 * np.sin(x_norm))))
        
        # Gaussian-like penalty with adaptive variance
        f19 = 0.3 * np.sum(np.exp(-0.5 * (x_norm / (1 + np.abs(x_norm) + 0.1))**2))
        
        # Mixed high-order and low-order interactions
        f20 = 0.1 * np.sum(x_norm**6 * np.sin(x_norm))
        
        # Fractional dimensionality effect
        f21 = 0.1 * np.sum(np.abs(x_norm)**(1.3 + 0.7 * np.sin(np.arange(self.dim) * 0.5)))
        
        # Adaptive chaotic coupling
        f22 = 0.15 * np.sum(np.sin(x_norm * np.cos(x_norm * 2)) * np.exp(-0.1 * np.abs(x_norm)))
        
        # Multi-scale oscillation with dynamic frequency
        f23 = 0.2 * np.sum(np.sin(30 * x_norm * np.log(1 + np.abs(x_norm))))
        
        # Enhanced penalty with asymmetric behavior
        f24 = 0.25 * np.sum(np.exp(-0.3 * (x_norm**2 + 0.1 * np.abs(x_norm))))
        
        # Complex cross-term interactions
        f25 = 0.05 * np.sum(np.sin(x_norm[:-2] * x_norm[1:-1] * x_norm[2:]))
        
        # Logarithmic polynomial interaction
        f26 = 0.1 * np.sum(np.log(1 + np.abs(x_norm)) * x_norm**3)
        
        # Hyperbolic tangent based chaotic interaction
        f27 = 0.12 * np.sum(np.tanh(x_norm * np.sin(x_norm)))
        
        # Fractional-order derivative inspired term
        f28 = 0.08 * np.sum(np.abs(x_norm)**1.9 * np.cos(x_norm))
        
        # Multi-modal sine with varying amplitude
        f29 = 0.18 * np.sum(np.sin(10 * x_norm + np.sin(5 * x_norm)) * np.exp(-0.2 * x_norm**2))
        
        # Adaptive scaling with exponential decay
        f30 = 0.1 * np.sum(np.exp(-0.5 * np.abs(x_norm)) * np.sin(15 * x_norm))
        
        # Novel chaotic coupling with dynamic phase modulation
        phase_mod = np.sin(np.arange(self.dim) * 0.3 + x_norm)
        f31 = 0.22 * np.sum(np.sin(x_norm * phase_mod) * np.cos(x_norm * np.sin(phase_mod)))
        
        # Fractional dimensionality with dynamic scaling
        dynamic_scale = 1.0 + 0.5 * np.sin(np.arange(self.dim) * 0.7)
        f32 = 0.12 * np.sum(np.abs(x_norm)**(1.5 + dynamic_scale * 0.8))
        
        # Multi-scale chaotic interaction with varying frequency bands
        f33 = 0.18 * np.sum(np.sin(50 * x_norm * np.cos(20 * x_norm)) * np.exp(-0.2 * np.abs(x_norm)))
        
        # Asymmetric penalty with dynamic threshold
        threshold = 0.5 + 0.3 * np.sin(np.arange(self.dim) * 0.4)
        f34 = 0.2 * np.sum(np.exp(-np.abs(x_norm - threshold) * 2))
        
        # Enhanced cross-dimensional coupling with hyperbolic interactions
        f35 = 0.1 * np.sum(np.tanh(x_norm[:-1] * x_norm[1:]) * np.sin(x_norm[:-1] + x_norm[1:]))
        
        # Dynamic power-law with time-varying exponents
        time_var = 2.0 + 1.5 * np.cos(np.arange(self.dim) * 0.2)
        f36 = 0.07 * np.sum(np.abs(x_norm)**time_var)
        
        # Multi-modal sine with complex amplitude modulation
        f37 = 0.15 * np.sum(np.sin(12 * x_norm + np.sin(8 * x_norm) + np.cos(4 * x_norm)) * np.exp(-0.3 * x_norm**2))
        
        # Adaptive chaotic frequency with exponential modulation
        f38 = 0.2 * np.sum(np.sin(20 * x_norm * np.exp(-0.1 * np.abs(x_norm))) * np.cos(15 * x_norm * np.exp(-0.05 * np.abs(x_norm))))
        
        # Fractional-order chaotic interaction with dynamic coupling
        f39 = 0.1 * np.sum(np.abs(x_norm)**(1.8 + 0.2 * np.sin(np.arange(self.dim) * 0.6)) * np.sin(x_norm * np.cos(x_norm)))
        
        # Complex multi-scale penalty with variable decay rates
        f40 = 0.18 * np.sum(np.exp(-0.4 * np.abs(x_norm) * (1 + 0.2 * np.sin(x_norm))))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15 + f16 + f17 + f18 + f19 + f20 + f21 + f22 + f23 + f24 + f25 + f26 + f27 + f28 + f29 + f30 + f31 + f32 + f33 + f34 + f35 + f36 + f37 + f38 + f39 + f40