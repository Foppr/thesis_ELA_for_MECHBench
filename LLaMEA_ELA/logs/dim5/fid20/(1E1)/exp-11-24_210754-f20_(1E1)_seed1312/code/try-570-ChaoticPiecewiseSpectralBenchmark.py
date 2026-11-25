import numpy as np

class ChaoticPiecewiseSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Piecewise polynomial base with chaotic breakpoints
        breakpoints = np.sin(np.linspace(0, np.pi, self.dim)) * 3.0
        f1 = 0.25 * np.sum(np.piecewise(x, [x <= breakpoints], [lambda x: x**3, lambda x: x**2]))
        
        # Dynamic gradient modulation with time-varying coefficients
        t = np.sum(x) / self.dim
        grad_mod = 1.0 + 0.3 * np.sin(2.0 * t) + 0.2 * np.cos(1.5 * t)
        f2 = 0.3 * np.sum(grad_mod * x**4 / self.dim)
        
        # Spectral coupling with frequency-varying harmonics
        freqs = 1.0 + 0.5 * np.sin(0.7 * x) + 0.3 * np.cos(0.4 * x)
        f3 = 0.2 * np.sum(np.sin(freqs * x) * np.cos(1.2 * x) * np.exp(-0.1 * x**2))
        
        # Chaotic sine-cosine interaction with dynamic phase shifts
        phase_shifts = 0.5 + 0.2 * np.sin(0.3 * x)
        f4 = 0.25 * np.sum(np.sin(x + phase_shifts) * np.cos(x - phase_shifts) * 
                          (1.0 + 0.1 * np.sin(0.5 * np.sum(x**2))))
        
        # Multi-scale polynomial shaping with adaptive exponents
        exponents = 2.0 + 0.4 * np.sin(0.6 * x)
        f5 = 0.18 * np.sum((x**exponents) / self.dim)
        
        # Cross-dimensional coupling with chaotic weight modulation
        weights = 1.0 + 0.2 * np.sin(0.8 * x[:-1] + 0.6 * x[1:])
        f6 = 0.2 * np.sum(weights * x[:-1]**1.5 * x[1:]**1.3 / self.dim)
        
        # Fractional harmonic interactions with dynamic resonance
        f7 = 0.15 * np.sum(np.sin(3.0 * x + np.cos(2.0 * x)) * 
                          np.cos(2.5 * x - np.sin(1.5 * x)) * 
                          (1.0 + 0.08 * np.sin(0.4 * np.sum(x**1.5))))
        
        # Asymmetric exponential coupling with variable scaling
        f8 = 0.17 * np.sum((np.exp(0.6 * x) - np.exp(-0.4 * x)) * 
                          np.sin(2.0 * x) * (1.0 + 0.05 * np.cos(1.5 * x)))
        
        # Dynamic polynomial with time-varying coefficients
        coeffs = 1.0 + 0.15 * np.sin(0.5 * t)
        f9 = 0.12 * np.sum((coeffs * x**3.5 + 0.3 * x**2.8) / self.dim)
        
        # Enhanced non-separability through coupled sine-cosine terms
        f10 = 0.14 * np.sum(np.sin(1.2 * x[:-1] + 0.8 * x[1:]) * 
                           np.cos(0.9 * x[:-1] - 0.7 * x[1:]) * 
                           (1.0 + 0.1 * np.sin(0.3 * np.sum(x))))
        
        # Chaotic modulation with feedback coupling
        f11 = 0.1 * np.sum(np.sin(2.5 * x + np.cos(1.8 * x)) * 
                          np.cos(2.2 * x - np.sin(1.6 * x)) * 
                          (1.0 + 0.06 * np.sin(0.2 * np.sum(x**2.3))))
        
        # Fractional cross-dimensional interactions with variable coupling
        f12 = 0.09 * np.sum((x[:-1]**2.1 * x[1:]**1.8 + x[:-1]**1.6 * x[1:]**2.2) / self.dim)
        
        # Adaptive harmonic modulation with dynamic frequency
        freq_mod = 1.5 + 0.3 * np.sin(0.4 * t)
        f13 = 0.13 * np.sum(np.sin(freq_mod * x) * np.cos(1.8 * x) * 
                           (1.0 + 0.07 * np.sin(0.5 * np.sum(x**1.7))))
        
        # Additional chaotic interference with modified scaling
        f14 = 0.08 * np.sum(np.sin(3.2 * x + np.cos(2.1 * x)) * 
                           np.cos(2.9 * x - np.sin(1.9 * x)) * 
                           np.cos(0.15 * np.sum(x**2.4)))
        
        # Enhanced spectral coupling with dynamic phase interaction
        f15 = 0.11 * np.sum(np.sin(2.3 * x + 0.5 * np.sin(1.3 * x)) * 
                           np.cos(2.1 * x - 0.4 * np.cos(1.2 * x)) * 
                           (1.0 + 0.09 * np.cos(0.6 * np.sum(x**1.9))))
        
        # Modified chaotic resonance with time-varying parameters
        f16 = 0.07 * np.sum(np.sin(3.5 * x + 0.2 * np.sin(2.3 * x)) * 
                           np.cos(3.1 * x - 0.3 * np.cos(1.8 * x)) * 
                           (1.0 + 0.05 * np.cos(0.4 * np.sum(x**2.2))))
        
        # Additional piecewise harmonic interaction
        f17 = 0.06 * np.sum(np.piecewise(x, [x <= 0], [lambda x: x**2.7, lambda x: x**3.1]))
        
        # Final chaotic gradient modulation with adaptive scaling
        f18 = 0.1 * np.sum((np.exp(0.4 * x) - np.exp(-0.2 * x)) * 
                          np.sin(1.8 * x) * (1.0 + 0.08 * np.cos(1.3 * x)))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15 + f16 + f17 + f18