import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion with Hermite polynomials
        hermite_poly = np.sum(x**2 + 2*x**3 + 0.5*x**4 + 0.1*x**5) / self.dim
        
        # Radial basis function component with Gaussian kernels
        rbf = 0.0
        centers = np.random.uniform(-5, 5, (5, self.dim))
        for i in range(5):
            rbf += np.exp(-np.sum((x - centers[i])**2) / (2 * 0.5**2))
        rbf /= 5
        
        # Sine-cosine coupling with varying frequencies and amplitudes
        sc_coupling = 0.0
        for i in range(self.dim):
            sc_coupling += np.sin(x[i]) * np.cos(3 * x[i]) + 0.5 * np.sin(2 * x[i]) * np.cos(x[i])
        sc_coupling /= self.dim
        
        # Cross-dimensional interaction with polynomial coupling
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            cross_interaction += (x[i]**2 + x[i+1]**2) * np.sin(x[i] * x[i+1])
        cross_interaction /= (self.dim - 1)
        
        # Chaotic sine modulation with varying periods
        chaotic_mod = 0.0
        for i in range(self.dim):
            chaotic_mod += np.sin(10 * x[i] + np.sin(7 * x[i])) * np.exp(-x[i]**2 / 2)
        chaotic_mod /= self.dim
        
        # Asymmetric polynomial potential with different exponents
        asym_potential = 0.0
        for i in range(self.dim):
            if x[i] >= 0:
                asym_potential += x[i]**3 + 0.5 * x[i]**4
            else:
                asym_potential += 0.8 * x[i]**3 + 0.3 * x[i]**5
        asym_potential /= self.dim
        
        # Multi-scale oscillatory component
        oscillatory = 0.0
        for i in range(self.dim):
            oscillatory += np.sin(15 * x[i]) + 0.7 * np.sin(25 * x[i]) + 0.3 * np.sin(40 * x[i])
        oscillatory /= self.dim
        
        # Combined result with weighted components
        result = (hermite_poly + rbf + sc_coupling + cross_interaction + 
                 chaotic_mod + asym_potential + oscillatory)
        
        # Add global minimum perturbation for enhanced challenge
        perturbation = 0.1 * np.sum(np.sin(x) * np.cos(2 * x) * np.exp(-x**2))
        result += perturbation
        
        return float(result)