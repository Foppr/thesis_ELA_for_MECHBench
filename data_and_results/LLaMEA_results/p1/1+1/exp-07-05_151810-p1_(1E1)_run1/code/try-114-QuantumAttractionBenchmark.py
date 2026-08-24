import numpy as np

class QuantumAttractionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component with Hermite polynomials
        chaos = 0.0
        for i in range(self.dim):
            # Hermite polynomial of degree 3
            H3 = 2 * x[i]**3 - 3 * x[i]
            chaos += 0.3 * H3 * np.exp(-0.1 * x[i]**2)
        
        # Gradient-based attraction field with multiple local minima
        attraction = 0.0
        for i in range(self.dim):
            # Multiple attraction centers with varying strengths
            center1 = 1.5 * np.sin(0.5 * i)
            center2 = 2.0 * np.cos(0.3 * i)
            dist1 = (x[i] - center1)**2
            dist2 = (x[i] - center2)**2
            attraction += 0.4 * np.exp(-0.5 * dist1) + 0.3 * np.exp(-0.3 * dist2)
        
        # Quantum-inspired oscillatory component with phase coupling
        quantum = 0.0
        for i in range(self.dim):
            if i == 0:
                phase = 0.0
            else:
                phase = 0.5 * np.sin(x[i-1]) + 0.3 * np.cos(x[i-1])
            quantum += 0.5 * np.sin(2.0 * x[i] + phase) * np.cos(1.5 * x[i] + 0.2 * np.sin(phase))
        
        # Dynamic basin boundaries with adaptive scaling
        basin = 0.0
        for i in range(self.dim):
            # Adaptive scaling based on dimension
            scale = 1.0 + 0.2 * np.sin(0.4 * i)
            # Basin boundary with non-linear transformation
            boundary = np.abs(x[i]) - 2.0 * np.sin(0.3 * x[i])
            basin += scale * np.exp(-0.5 * boundary**2)
        
        # Adaptive coupling between dimensions with frequency modulation
        coupling = 0.0
        for i in range(self.dim):
            if i > 0:
                # Frequency modulation based on previous dimension
                freq_mod = 1.0 + 0.1 * np.sin(0.5 * x[i-1])
                coupling += 0.2 * np.sin(freq_mod * x[i]) * np.cos(0.3 * x[i-1])
        
        # Combine all components with dynamic weights
        weight_chaos = 1.0 + 0.1 * np.sin(0.2 * np.sum(x))
        weight_attraction = 1.0 + 0.05 * np.cos(0.3 * np.sum(x))
        weight_quantum = 1.0 + 0.15 * np.sin(0.25 * np.sum(x))
        weight_basin = 1.0 + 0.1 * np.cos(0.4 * np.sum(x))
        weight_coupling = 1.0 + 0.08 * np.sin(0.35 * np.sum(x))
        
        result = weight_chaos * chaos + weight_attraction * attraction + weight_quantum * quantum + weight_basin * basin + weight_coupling * coupling
        
        return result