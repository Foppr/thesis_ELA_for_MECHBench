import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        result = np.sum(x**2)
        
        # Chaotic sine-cosine interaction terms with varying frequencies
        chaotic_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_terms += np.sin(2.0 * np.pi * x[i]) * np.cos(3.0 * np.pi * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        result += 0.5 * chaotic_terms
        
        # Polynomial chaos with mixed even/odd powers
        poly_chaos = 0.0
        for i in range(self.dim):
            poly_chaos += (x[i]**3 + 0.3 * x[i]**5 + 0.05 * x[i]**7) * np.sin(0.5 * np.pi * x[i])
        result += 0.3 * poly_chaos
        
        # Adaptive radial basis function perturbations
        rbf_perturb = 0.0
        centers = np.linspace(-5.0, 5.0, 5)
        for i in range(self.dim):
            for center in centers:
                rbf_perturb += np.exp(-0.5 * ((x[i] - center) / 1.5)**2) * np.cos(2.0 * np.pi * (x[i] - center))
        result += 0.4 * rbf_perturb
        
        # Multi-scale oscillatory component with frequency modulation
        oscillatory = 0.0
        for i in range(self.dim):
            oscillatory += np.sin(10.0 * x[i]) * np.cos(5.0 * x[i]) * np.exp(-0.2 * x[i]**2)
        result += 0.25 * oscillatory
        
        # Asymmetric multimodal peaks with exponential decay
        peaks = 0.0
        for i in range(self.dim):
            peaks += np.exp(-0.5 * (x[i] - 2.0)**2) * np.sin(4.0 * np.pi * x[i])**2 + \
                     np.exp(-0.5 * (x[i] + 2.0)**2) * np.cos(3.0 * np.pi * x[i])**2
        result += 0.3 * peaks
        
        # Coupling terms with hyperbolic tangent modulation
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += np.tanh(x[i]) * np.sin(x[i+1]) * np.exp(-0.1 * (x[i] - x[i+1])**2)
        result += 0.2 * coupling
        
        # High-order polynomial with chaotic coefficients
        high_order = 0.0
        coeffs = [1.0, 0.5, 0.1, 0.02, 0.005]
        for i in range(self.dim):
            for j, coeff in enumerate(coeffs):
                high_order += coeff * x[i]**(2*j + 1) * np.sin(0.1 * x[i])
        result += 0.15 * high_order
        
        return result