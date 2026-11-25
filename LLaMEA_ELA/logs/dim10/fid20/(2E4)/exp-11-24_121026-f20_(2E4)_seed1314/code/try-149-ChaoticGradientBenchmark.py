import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Enhanced multimodal component with higher frequency trigonometric coupling
        f2 = np.sum((np.sin(25 * x_norm) * np.cos(15 * x_norm) + 0.7 * np.sin(35 * x_norm))**6)
        
        # Exponential decay with sinusoidal modulation for ruggedness
        f3 = np.sum(np.exp(-x_norm**2) * (1 + 0.5 * np.sin(25 * x_norm) * np.cos(19 * x_norm)))
        
        # Polynomial with cross-dimensional coupling and chaotic interaction
        f4 = np.sum((x_norm**4 + 0.6 * x_norm**3 - 0.4 * x_norm**2)**2 * (1 + 0.4 * np.sin(27 * x_norm)))
        
        # Hyperbolic tangent with dynamic scaling for smooth transitions
        f5 = np.sum(np.tanh(12 * x_norm) * (1 + 0.4 * np.cos(19 * x_norm))**4)
        
        # Cross-dimensional interaction with dynamic weights and chaotic coupling
        weights = 1 / (1 + np.exp(-8 * (x_norm[:-1] - x_norm[1:])))  # Steeper weight function
        f6 = 1.2 * np.sum((x_norm[:-1]**3 + x_norm[1:]**3)**2 * weights)
        
        # Fractional power with logarithmic barrier
        f7 = 0.8 * np.sum(np.abs(x_norm)**2.1 * (1 + 0.3 * np.sin(21 * x_norm)))
        
        # Nested trigonometric chaos with multiple frequencies
        f8 = 0.6 * np.sum(np.sin(np.pi * x_norm * np.sin(13 * x_norm))**7)
        
        # Mixed polynomial and exponential with enhanced nonlinearity
        f9 = 0.4 * np.sum((x_norm**5 - 0.7 * x_norm**4 + 0.3 * x_norm**3)**2 * np.exp(-0.6 * x_norm**2))
        
        # Enhanced gradient-based chaotic modulation with boundary influence
        f10 = 0.35 * np.sum(np.sin(28 * x_norm) * np.cos(19 * x_norm) * np.exp(-0.8 * x_norm**2))
        
        # Multi-scale sinusoidal term for fine-grained complexity
        f11 = 0.3 * np.sum(np.sin(35 * x_norm + np.sin(17 * x_norm))**6)
        
        # Additional chaotic coupling with nested dynamics
        logistic_map = 4 * x_norm * (1 - x_norm)
        f12 = 0.25 * np.sum(np.sin(logistic_map * 8.5) * np.cos(logistic_map * 12.5))  # Slightly altered frequencies
        
        # Additional high-frequency chaotic modulation
        f13 = 0.2 * np.sum(np.sin(40 * x_norm) * np.cos(30 * x_norm) * np.exp(-0.9 * x_norm**2))
        
        # Nested polynomial chaos with higher-order terms
        f14 = 0.15 * np.sum((x_norm**6 + 0.5 * x_norm**5 - 0.3 * x_norm**4)**2)
        
        # Return weighted combination of all components
        return f1 + 0.7 * f2 + 0.6 * f3 + 0.5 * f4 + 0.45 * f5 + 0.4 * f6 + 0.35 * f7 + 0.32 * f8 + 0.28 * f9 + 0.25 * f10 + 0.22 * f11 + 0.18 * f12 + 0.15 * f13 + 0.12 * f14