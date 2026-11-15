import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial base with mixed degrees for conditioning
        poly_base = np.sum(x_norm**4 + 0.5 * x_norm**3 + 0.2 * x_norm**2)
        
        # Chaotic sine-cosine interaction terms with varying coupling strengths
        chaotic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Nonlinear coupling with chaotic modulation
                coupling = np.sin(5 * x_norm[i]) * np.cos(7 * x_norm[j]) * np.exp(-0.1 * (x_norm[i]**2 + x_norm[j]**2))
                chaotic_interaction += coupling * (1 + 0.2 * np.sin(13 * (x_norm[i] + x_norm[j])))
        
        # Composite multimodal structure with polynomial and trigonometric components
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += (x_norm[i]**6 - 2 * x_norm[i]**4 + x_norm[i]**2) * np.sin(10 * x_norm[i])
        
        # Adaptive conditioning with dynamic scaling factors
        adaptive = 0.0
        for i in range(self.dim):
            adaptive += (1 + 0.3 * np.sin(2 * x_norm[i])) * x_norm[i]**3
        
        # Cross-dimensional interaction with phase-shifted trigonometric terms
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            cross_interaction += np.sin(x_norm[i] + x_norm[i+1] + 0.7) * np.cos(x_norm[i] - x_norm[i+1] - 0.4)
        
        # Global optimum perturbation with chaotic oscillation
        global_pert = np.sum(np.sin(15 * x_norm)**2 + np.cos(15 * x_norm)**2 + 0.5 * np.sin(30 * x_norm))
        
        # Combined weighted components
        return 0.5 * poly_base + 1.2 * chaotic_interaction + 1.8 * multimodal + 0.9 * adaptive + 0.7 * cross_interaction + 1.5 * global_pert