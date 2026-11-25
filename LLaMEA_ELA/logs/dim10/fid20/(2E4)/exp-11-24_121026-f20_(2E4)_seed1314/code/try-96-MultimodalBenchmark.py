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
        f2 = np.sum(np.sin(60 * np.pi * x_norm)**9)
        
        # Exponential barrier terms to create rugged landscape
        f3 = np.sum(np.exp(-x_norm**2) - 1.0)
        
        # Mixed polynomial and trigonometric terms for additional complexity
        f4 = np.sum(x_norm**10 * np.cos(8 * np.pi * x_norm))
        
        # Add a global repulsion term to prevent easy convergence
        f5 = 0.6 * np.sum(np.abs(x_norm)**0.3)
        
        # Additional high-frequency component for increased complexity
        f6 = 0.4 * np.sum(np.sin(50 * x_norm**2) * np.cos(20 * x_norm))
        
        # Add a new chaotic term with modified logistic map-like behavior
        f7 = 0.6 * np.sum(np.sin(np.pi * x_norm * np.sin(35 * x_norm))**7)
        
        # Add a fourth-order polynomial with random coefficients for extra ruggedness
        f8 = 0.15 * np.sum((x_norm**4 + 0.9 * x_norm**3 - 0.7 * x_norm**2 + 0.4 * x_norm)**2)
        
        # Introduce a new chaotic logistic-like component with different parameters for better fitness
        f9 = 0.5 * np.sum(np.sin(10 * np.pi * x_norm * np.sin(25 * x_norm**2))**10)
        
        # Add a new sinusoidal modulation with variable frequency
        f10 = 0.2 * np.sum(np.sin(30 * x_norm * np.cos(10 * x_norm))**6)
        
        # Introduce a fractional polynomial term to enhance non-smoothness
        f11 = 0.15 * np.sum(np.abs(x_norm)**2.1)
        
        # Add a logarithmic barrier for additional complexity near boundaries
        f12 = 0.25 * np.sum(np.log(1 + x_norm**2))
        
        # New: Introduce cross-dimensional interaction terms for higher complexity
        f13 = 0.2 * np.sum((x_norm[:-1] + x_norm[1:]) ** 5)
        
        # New: Add a quintic chaotic term with multiple nested frequencies
        f14 = 0.3 * np.sum(np.sin(4 * np.pi * x_norm * np.sin(20 * x_norm) * np.sin(30 * x_norm))**6)
        
        # New: Introduce a hyperbolic tangent modulation for enhanced nonlinearity
        f15 = 0.15 * np.sum(np.tanh(12 * x_norm)**4)
        
        # New: Introduce a new chaotic sine term with increased frequency and modified amplitude
        f16 = 0.35 * np.sum(np.sin(70 * x_norm * np.sin(25 * x_norm**3))**8)
        
        # New: Add a new interaction term with cubic cross-terms for enhanced complexity
        f17 = 0.15 * np.sum((x_norm[:-2] + x_norm[1:-1] + x_norm[2:]) ** 4)
        
        # New: Introduce a modified Gaussian-like barrier for additional ruggedness
        f18 = 0.3 * np.sum(np.exp(-x_norm**5) - 1.0)
        
        # New: Add a new hyperbolic secant term for enhanced nonlinearity and complexity
        f19 = 0.2 * np.sum(np.sech(15 * x_norm)**3)
        
        # New: Introduce a new trigonometric composition with nested sine and cosine functions
        f20 = 0.18 * np.sum(np.sin(40 * np.cos(12 * x_norm))**5)
        
        return (f1 + 0.5 * f2 + 0.25 * f3 + 0.2 * f4 + 0.15 * f5 + 
                0.06 * f6 + 0.2 * f7 + 0.06 * f8 + 0.25 * f9 + 0.1 * f10 + 
                0.12 * f11 + 0.25 * f12 + 0.12 * f13 + 0.18 * f14 + 0.1 * f15 + 
                0.12 * f16 + 0.06 * f17 + 0.18 * f18 + 0.15 * f19 + 0.1 * f20)