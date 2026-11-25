import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute graph Laplacian eigenvalues for spectral components
        self.laplacian_eigenvals = np.array([1.0 + i * 0.1 for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Spectral graph-based potential wells
        spectral = 0
        for i in range(self.dim):
            eigenval = self.laplacian_eigenvals[i % len(self.laplacian_eigenvals)]
            spectral += eigenval * np.sin(x[i]) * np.cos(0.5 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Evolutionary dynamics with fitness-dependent selection pressure
        evolutionary = 0
        for i in range(self.dim):
            selection_pressure = 1.0 + 0.5 * np.sin(x[i])
            evolutionary += selection_pressure * (x[i]**4 - 6*x[i]**2 + 9) * np.exp(-0.05 * x[i]**2)
        
        # Quantum field interaction potential with multi-scale coupling
        quantum = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                distance = np.abs(x[i] - x[j])
                quantum += np.exp(-distance**2) * np.sin(2.0 * (x[i] + x[j])) * np.cos(0.5 * (x[i] - x[j]))
        
        # Topologically complex ridge structures with torsion
        topology = 0
        for i in range(self.dim):
            torsion = np.sin(0.3 * x[i]) * np.cos(0.7 * x[i])
            topology += torsion * (x[i]**5 - 2*x[i]**3 + x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Multi-modal basin coupling with dynamic threshold
        basin = 0
        for i in range(self.dim):
            threshold = 2.0 + 1.5 * np.sin(0.4 * x[i])
            basin += (x[i] > threshold) * (x[i]**3 - 3*x[i]) + (x[i] <= threshold) * (x[i]**2 - 1)
        
        # Adaptive resonance components with chaotic frequency modulation
        resonance = 0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.3 * np.sin(0.8 * x[i])
            resonance += np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i]**2) * np.exp(-0.08 * x[i]**2)
        
        # Combine all components with dynamic weighting
        weights = [0.2, 0.15, 0.25, 0.18, 0.12, 0.08 + 0.02 * np.sin(0.3 * sum(x))]
        return (weights[0] * spectral + 
                weights[1] * evolutionary + 
                weights[2] * quantum + 
                weights[3] * topology + 
                weights[4] * basin + 
                weights[5] * resonance)