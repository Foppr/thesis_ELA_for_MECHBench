import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.frac_order = 0.3 + np.random.rand() * 0.4
        self.quantum_strength = 2.0 + np.random.rand() * 3.0
        self.memory_decay = 0.1 + np.random.rand() * 0.2
        self.hyperchaos_param = 4.0 + np.random.rand() * 2.0
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractional-order chaotic component with hyperchaotic tent map
        frac_chaos = 0.0
        for i in range(self.dim):
            base = np.sin(i * self.hyperchaos_param)
            frac_chaos += np.power(np.abs(x[i]), self.frac_order) * base
        
        # Quantum interference pattern with adaptive phase
        quantum_interference = 0.0
        for i in range(self.dim):
            phase = np.sin(i * self.quantum_strength + np.sum(x) * 0.1)
            quantum_interference += np.sin(x[i] * 2.0 + phase) * np.cos(x[i] * 1.5 + phase)
        
        # Memory-dependent elliptic potential with decay factor
        memory_elliptic = 0.0
        for i in range(self.dim):
            memory_factor = np.exp(-self.memory_decay * i)
            scale = 1.0 + memory_factor * np.sin(i * 0.7)
            memory_elliptic += scale * x[i]**2 * (np.cos(x[i]) + 1.0)
        
        # Cross-dimensional coupling with fractional weights
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.power(np.abs(x[i] - x[j]), self.frac_order)
                cross_coupling += weight * np.sin((x[i] + x[j]) * 0.3)
        
        # Adaptive fitness scaling with time-varying parameters
        time_factor = np.sin(np.sum(x) * 0.2) * 0.5 + 1.0
        scale_factor = 1.0 + np.abs(np.sin(self.dim * 0.1)) * 0.3
        
        # Combine all components with dynamic weighting
        result = (0.3 * frac_chaos + 
                 0.3 * quantum_interference + 
                 0.2 * memory_elliptic + 
                 0.2 * cross_coupling) * time_factor * scale_factor
        
        return result