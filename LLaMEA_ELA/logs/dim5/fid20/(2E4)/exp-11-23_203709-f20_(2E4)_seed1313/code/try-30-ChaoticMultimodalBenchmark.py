import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logarithmic barrier components
        barriers = 0
        for i in range(self.dim):
            barriers += np.log(1 + (x[i] - 3.0)**2) + np.log(1 + (x[i] + 3.0)**2)
        
        # Trigonometric coupling terms with adaptive frequencies
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                coupling += np.sin(x[i] * x[j]) * np.cos(2 * x[i] + x[j])
        
        # Adaptive peak locations based on dimension
        peaks = 0
        for i in range(self.dim):
            peak_pos = 2.5 * np.sin(i * np.pi / self.dim)
            peaks += (x[i] - peak_pos)**2 * np.exp(-0.5 * (x[i] - peak_pos)**2)
        
        # Chaotic component using sine maps
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(10 * np.sin(x[i])) * np.cos(5 * x[i])
        
        # Combine all components with appropriate scaling
        return 2.5 * barriers + 3.0 * coupling + 1.5 * peaks + 0.8 * chaotic + 15 * self.dim