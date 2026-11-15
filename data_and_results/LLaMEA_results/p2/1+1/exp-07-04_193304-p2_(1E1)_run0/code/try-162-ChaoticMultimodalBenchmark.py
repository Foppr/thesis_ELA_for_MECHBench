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
        freqs = np.arange(1, self.dim + 1) * np.pi * 1.5  # Increased frequencies
        f5 = np.sum(np.sin(freqs * x_norm))
        f6 = np.sum(np.cos(freqs * x_norm))
        
        # Chaotic interaction using sine and cosine combinations
        f7 = np.sum(np.sin(x_norm * np.sin(x_norm * 0.9)))  # Slight modification
        f8 = np.sum(np.cos(x_norm * np.cos(x_norm * 1.5)))  # Slight modification
        
        # Exponential decay with varying rates
        rates = np.arange(1, self.dim + 1) * 0.3  # Increased rates
        f9 = np.sum(np.exp(-rates * np.abs(x_norm)))
        
        # Cross-dimensional interactions with non-linear coupling
        f10 = 0.15 * np.sum(np.sin(x_norm[:-1] * x_norm[1:]))  # Increased coefficient
        f11 = 0.10 * np.sum(np.cos(x_norm[:-1] * x_norm[1:]))  # Increased coefficient
        
        # High-frequency oscillation with amplitude modulation
        f12 = np.sum(np.sin(25 * x_norm) * np.exp(-0.5 * x_norm**2))  # Increased frequency, modified decay
        
        # Power-law interaction with varying exponents
        f13 = 0.08 * np.sum(np.abs(x_norm)**(3.9 + np.sin(np.arange(self.dim)) * 2.0))  # Modified exponent range
        
        # Additional chaotic sine-cosine interaction
        f14 = 0.25 * np.sum(np.sin(18 * x_norm) * np.cos(15 * x_norm))  # Modified frequencies
        
        # Modified exponential term with logarithmic scaling
        f15 = 0.18 * np.sum(np.exp(-np.abs(x_norm) * np.log(1.3 + np.abs(x_norm))))  # Modified log base
        
        # Combined polynomial and trigonometric term
        f16 = 0.13 * np.sum((x_norm**2 + np.sin(x_norm))**2)
        
        # Fractional power term for added complexity
        f17 = 0.11 * np.sum(np.abs(x_norm)**1.7)  # Slightly reduced exponent
        
        # Non-uniform frequency sine term
        f18 = 0.30 * np.sum(np.sin(28 * x_norm * (1 + 0.15 * np.sin(x_norm))))  # Increased frequency and factor
        
        # Gaussian-like penalty with adaptive variance
        f19 = 0.35 * np.sum(np.exp(-0.5 * (x_norm / (1.2 + np.abs(x_norm) + 0.2))**2))  # Modified denominator
        
        # Mixed high-order and low-order interactions
        f20 = 0.13 * np.sum(x_norm**6 * np.sin(x_norm * 1.0))  # Slight modification
        
        # Fractional dimensionality effect
        f21 = 0.13 * np.sum(np.abs(x_norm)**(1.5 + 0.7 * np.sin(np.arange(self.dim) * 0.7)))  # Modified sine factor
        
        # Adaptive chaotic coupling
        f22 = 0.18 * np.sum(np.sin(x_norm * np.cos(x_norm * 2.3)) * np.exp(-0.15 * np.abs(x_norm)))  # Modified coupling
        
        # Multi-scale oscillation with dynamic frequency
        f23 = 0.25 * np.sum(np.sin(35 * x_norm * np.log(1.2 + np.abs(x_norm))))  # Increased frequency and log base
        
        # Enhanced penalty with asymmetric behavior
        f24 = 0.28 * np.sum(np.exp(-0.35 * (x_norm**2 + 0.15 * np.abs(x_norm))))  # Modified parameters
        
        # Complex cross-term interactions
        f25 = 0.08 * np.sum(np.sin(x_norm[:-2] * x_norm[1:-1] * x_norm[2:]))  # Increased coefficient
        
        # Logarithmic polynomial interaction
        f26 = 0.13 * np.sum(np.log(1.2 + np.abs(x_norm)) * x_norm**3)  # Modified log base
        
        # Hyperbolic tangent based chaotic interaction
        f27 = 0.15 * np.sum(np.tanh(x_norm * np.sin(x_norm * 1.2)))  # Slight modification
        
        # Fractional-order derivative inspired term
        f28 = 0.11 * np.sum(np.abs(x_norm)**1.9 * np.cos(x_norm * 1.1))  # Slight modification
        
        # Multi-modal sine with varying amplitude
        f29 = 0.22 * np.sum(np.sin(13 * x_norm + np.sin(7 * x_norm)) * np.exp(-0.25 * x_norm**2))  # Increased frequencies
        
        # Adaptive scaling with exponential decay
        f30 = 0.13 * np.sum(np.exp(-0.5 * np.abs(x_norm)) * np.sin(18 * x_norm))  # Modified decay and frequency
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15 + f16 + f17 + f18 + f19 + f20 + f21 + f22 + f23 + f24 + f25 + f26 + f27 + f28 + f29 + f30