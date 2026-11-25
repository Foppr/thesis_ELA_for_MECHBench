import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Quadratic term with conditioning
        f1 = np.sum(x_norm**2)
        
        # High-frequency sinusoidal terms with multiple local minima
        f2 = np.sum(np.sin(50 * np.pi * x_norm)**8)
        
        # Exponential barrier terms to create rugged landscape
        f3 = np.sum(np.exp(-x_norm**2) - 1.0)
        
        # Mixed polynomial and trigonometric terms for additional complexity
        f4 = np.sum(x_norm**9 * np.cos(7 * np.pi * x_norm))
        
        # Add a global repulsion term to prevent easy convergence
        f5 = 0.5 * np.sum(np.abs(x_norm)**0.4)
        
        # Additional high-frequency component for increased complexity
        f6 = 0.3 * np.sum(np.sin(45 * x_norm**2) * np.cos(15 * x_norm))
        
        # Add a new chaotic term with modified logistic map-like behavior
        f7 = 0.5 * np.sum(np.sin(np.pi * x_norm * np.sin(30 * x_norm))**7)
        
        # Add a fourth-order polynomial with random coefficients for extra ruggedness
        f8 = 0.08 * np.sum((x_norm**4 + 0.8 * x_norm**3 - 0.6 * x_norm**2 + 0.3 * x_norm)**3)
        
        # Introduce a new chaotic logistic-like component with different parameters for better fitness
        f9 = 0.4 * np.sum(np.sin(10 * np.pi * x_norm * np.sin(25 * x_norm**2))**9)
        
        # Add a new sinusoidal modulation with variable frequency
        f10 = 0.15 * np.sum(np.sin(25 * x_norm * np.cos(10 * x_norm))**5)
        
        # Introduce a fractional polynomial term to enhance non-smoothness
        f11 = 0.1 * np.sum(np.abs(x_norm)**1.9)
        
        # Add a logarithmic barrier for additional complexity near boundaries
        f12 = 0.2 * np.sum(np.log(1 + x_norm**2))
        
        # Introduce a novel chaotic component with enhanced frequency modulation and nonlinearity
        f13 = 0.3 * np.sum(np.sin(5 * np.pi * x_norm * np.sin(20 * x_norm**3))**10)
        
        # Add a modified hyperbolic tangent term for additional ruggedness
        f14 = 0.2 * np.sum(np.tanh(4 * x_norm)**4)
        
        # Add a new chaotic sine-cosine hybrid component
        f15 = 0.25 * np.sum(np.sin(3 * np.pi * x_norm * np.cos(18 * x_norm**2))**6)
        
        # Add a fifth-order polynomial with variable coefficients
        f16 = 0.05 * np.sum((x_norm**5 + 0.6 * x_norm**4 - 0.4 * x_norm**3 + 0.2 * x_norm**2 - 0.1 * x_norm)**2)
        
        # Add a complex interaction term between dimensions
        f17 = 0.1 * np.sum(np.sin(np.pi * np.sum(x_norm**2, axis=0))**4)
        
        # Combine all terms with adjusted weights for maximum challenge
        return f1 + 0.5 * f2 + 0.25 * f3 + 0.15 * f4 + 0.12 * f5 + 0.05 * f6 + 0.18 * f7 + 0.06 * f8 + 0.22 * f9 + 0.08 * f10 + 0.12 * f11 + 0.2 * f12 + 0.2 * f13 + 0.15 * f14 + 0.15 * f15 + 0.07 * f16 + 0.1 * f17