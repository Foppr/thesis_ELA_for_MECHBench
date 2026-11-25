import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.hyperchaos_factor = 4.0 + np.random.rand() * 3.0
        self.quantum_phase = np.random.rand() * 2.0 * np.pi
        self.rbf_strength = 1.0 + np.random.rand() * 2.0
        self.polynomial_degree = 3 + np.random.randint(3)
        self.adaptive_scaling = 0.5 + np.random.rand() * 1.5
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperchaotic tent map component with quantum phase interference
        hyperchaos = 0.0
        for i in range(self.dim):
            tent_map = np.sin(i * self.hyperchaos_factor) * np.cos(x[i])
            phase_shift = np.sin(x[i] * self.quantum_phase)
            hyperchaos += tent_map * phase_shift
        
        # Quantum-inspired radial basis function with dynamic parameters
        rbf = 0.0
        for i in range(self.dim):
            center = np.sin(i * 0.7) * 2.0
            width = 0.5 + np.random.rand() * 1.5
            rbf += self.rbf_strength * np.exp(-width * (x[i] - center)**2)
        
        # Cross-dimensional polynomial coupling with adaptive scaling
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                term = (x[i] * x[j])**self.polynomial_degree
                weight = np.sin(i * j * 0.3) * self.adaptive_scaling
                poly_coupling += weight * term
        
        # Dynamic cosine wave with time-varying frequency and amplitude
        dynamic_cosine = 0.0
        for i in range(self.dim):
            freq = 2.0 + np.sin(i * 0.4) * 1.5
            amp = 1.0 + np.cos(i * 0.6) * 0.5
            dynamic_cosine += amp * np.cos(x[i] * freq) * np.sin(x[i] * 0.8)
        
        # Asymmetric exponential saddle point component
        saddle_point = 0.0
        for i in range(self.dim):
            saddle_point += np.exp(-np.abs(x[i]) * 0.5) * np.sin(x[i] * 1.2)
        
        # Combine all components with dynamic weighting and time-varying modifier
        time_modifier = 1.0 + 0.3 * np.sin(np.sum(x) * 0.1)
        result = (0.25 * hyperchaos + 
                 0.25 * rbf + 
                 0.20 * poly_coupling + 
                 0.20 * dynamic_cosine + 
                 0.10 * saddle_point) * time_modifier
        
        return result