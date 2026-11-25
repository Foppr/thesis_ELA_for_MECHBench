import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Multimodal component with dynamic scaling and chaotic modulation
        f2 = np.sum((np.sin(13 * x_norm) * np.cos(7 * x_norm) + 0.5 * np.sin(23 * x_norm))**4)
        
        # Exponential decay with sinusoidal modulation for ruggedness
        f3 = np.sum(np.exp(-x_norm**2) * (1 + 0.3 * np.sin(17 * x_norm) * np.cos(11 * x_norm)))
        
        # Polynomial with cross-dimensional coupling and chaotic interaction
        f4 = np.sum((x_norm**3 + 0.4 * x_norm**2 - 0.2 * x_norm)**2 * (1 + 0.25 * np.sin(19 * x_norm)))
        
        # Hyperbolic tangent with dynamic scaling for smooth transitions
        f5 = np.sum(np.tanh(8 * x_norm) * (1 + 0.3 * np.cos(14 * x_norm))**3)
        
        # Cross-dimensional interaction with dynamic weights and chaotic coupling
        weights = 1 / (1 + np.exp(-5 * (x_norm[:-1] - x_norm[1:])))
        f6 = 0.8 * np.sum((x_norm[:-1]**2 + x_norm[1:]**2)**2 * weights)
        
        # Fractional power with logarithmic barrier
        f7 = 0.6 * np.sum(np.abs(x_norm)**1.7 * (1 + 0.2 * np.sin(15 * x_norm)))
        
        # Nested trigonometric chaos with multiple frequencies
        f8 = 0.4 * np.sum(np.sin(np.pi * x_norm * np.sin(9 * x_norm))**5)
        
        # Mixed polynomial and exponential with enhanced nonlinearity
        f9 = 0.3 * np.sum((x_norm**4 - 0.6 * x_norm**3 + 0.2 * x_norm**2)**2 * np.exp(-0.5 * x_norm**2))
        
        # Enhanced gradient-based chaotic modulation with boundary influence
        f10 = 0.25 * np.sum(np.sin(20 * x_norm) * np.cos(13 * x_norm) * np.exp(-0.7 * x_norm**2))
        
        # Multi-scale sinusoidal term for fine-grained complexity
        f11 = 0.2 * np.sum(np.sin(25 * x_norm + np.sin(12 * x_norm))**4)
        
        # Additional chaotic coupling with nested dynamics
        logistic_map = 4 * x_norm * (1 - x_norm)
        f12 = 0.18 * np.sum(np.sin(logistic_map * 6.0) * np.cos(logistic_map * 9.0))
        
        # Return weighted combination of all components
        return f1 + 0.5 * f2 + 0.4 * f3 + 0.35 * f4 + 0.3 * f5 + 0.25 * f6 + 0.2 * f7 + 0.18 * f8 + 0.15 * f9 + 0.12 * f10 + 0.1 * f11 + 0.08 * f12