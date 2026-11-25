import numpy as np

class ChaoticRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with chaotic symmetry breaking
        r = np.sqrt(np.sum(x**2))
        radial_term = r * (1.0 + 0.3 * np.sin(10.0 * r) * np.cos(7.0 * r))
        
        # Multimodal sinusoidal landscape with adaptive frequency
        modal_term = np.sum(np.sin(3.0 * x + 0.5 * np.sin(2.0 * x)) * np.cos(2.0 * x + 0.4 * np.cos(3.0 * x)))
        
        # Adaptive cross-dimensional coupling with exponential scaling
        cross_coupling = 0.0
        for i in range(self.dim - 1):
            cross_coupling += np.exp(-0.1 * (x[i] - x[i+1])**2) * np.sin(5.0 * (x[i]**2 + x[i+1]**2))
        
        # Hybrid gradient-flow oscillations with hyperbolic scaling
        grad_flow = np.sum(np.tanh(x) * np.exp(-0.5 * x**2) * np.sin(4.0 * x) * np.cos(3.0 * x))
        
        # Chaotic perturbation with logistic map modulation
        chaotic_perturb = 0.0
        for i in range(self.dim):
            chaotic_perturb += np.sin(15.0 * x[i]) * np.cos(12.0 * x[i]) * (1.0 + 0.2 * np.sin(8.0 * x[i]))
        
        # Combined function with optimized weights for high multimodality and complexity
        return 0.4 * radial_term + 0.3 * modal_term + 0.15 * cross_coupling + 0.1 * grad_flow + 0.05 * chaotic_perturb