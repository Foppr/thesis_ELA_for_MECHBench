import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        result = np.sum(x**2)
        
        # Chaotic tent map perturbations with varying parameter
        tent_pert = 0.0
        for i in range(self.dim):
            if x[i] < 0.5:
                tent_val = 2.0 * x[i]
            else:
                tent_val = 2.0 * (1.0 - x[i])
            tent_pert += 0.5 * tent_val * np.sin(3.0 * np.pi * x[i])
        result += tent_pert
        
        # Fractional polynomial distortions with non-integer exponents
        poly_distortion = 0.8 * np.sum(x**2.5 + 0.3 * x**3.7 + 0.1 * x**4.2 + 0.05 * x**5.1)
        
        # Radial basis function interactions with Gaussian and multiquadric kernels
        rbf_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                rbf_interaction += 0.4 * np.exp(-0.5 * dist**2) + 0.2 * np.sqrt(dist**2 + 0.1)
        result += rbf_interaction
        
        # Enhanced multimodal peaks with modified hyperbolic secant functions
        peaks = 0.7 * np.sum(np.sech(2.0 * x)**2 * np.cos(3.0 * x)**3)
        
        # Novel sine-cosine coupling with phase modulation
        coupling = 0.5 * np.sum(np.sin(x[:-1] + 0.3 * x[1:]) * np.cos(x[:-1] * x[1:]) * np.sin(0.5 * x[:-1]))
        
        # Asymmetric chaotic perturbations using logistic map
        logistic_pert = 0.0
        for i in range(self.dim):
            logistic_val = 3.8 * x[i] * (1.0 - x[i])
            logistic_pert += 0.3 * logistic_val * np.cos(2.0 * np.pi * x[i])
        result += logistic_pert
        
        # Saddle point with modified hyperbolic functions
        saddle = 0.2 * np.sum(np.tanh(x)**2 * np.sinh(x)**2)
        
        # Novel fractional interaction term
        frac_interaction = 0.25 * np.sum(np.abs(x)**1.7 * np.sin(2.0 * x))
        
        # Combine all terms
        result = result + poly_distortion + rbf_interaction + peaks + coupling + logistic_pert + saddle + frac_interaction
        
        return result