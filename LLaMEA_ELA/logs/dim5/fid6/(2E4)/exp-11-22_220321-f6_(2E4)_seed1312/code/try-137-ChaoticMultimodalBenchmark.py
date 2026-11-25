import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.quantum_parameter = 0.8
        self.levy_alpha = 1.6
        self.elastic_modulus = 2.5
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired probability distribution component with enhanced interference
        quantum_term = 0.0
        for i in range(self.dim):
            prob_amp = np.sin(x[i] * self.quantum_parameter) ** 2 + np.cos(x[i] * self.quantum_parameter) ** 2
            quantum_term += prob_amp * np.exp(-0.3 * (x[i] - np.sin(i))**2)
        
        # Levy-flight based exploration component with improved heavy-tailed jumps
        levy_term = 0.0
        for i in range(self.dim):
            levy_jump = np.random.laplace(0, 1, 1)[0]
            levy_term += np.sin(x[i] * (1 + 0.3 * levy_jump)) * np.cos(x[i] * (1 + 0.2 * np.abs(levy_jump)))
        
        # Dynamic hyper-elastic strain fields with enhanced stiffness modulation
        elastic_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x[i] - x[j]
                stiffness = self.elastic_modulus * (1 + 0.6 * np.sin(i * j * 0.4))
                elastic_term += stiffness * (diff**2) * np.exp(-0.15 * np.abs(diff))
        
        # Multi-scale hyperbolic tangent oscillations with adaptive frequency modulation
        tanh_term = 0.0
        for i in range(self.dim):
            freq_mod = 1 + 0.4 * np.sin(i * 0.5)
            tanh_term += np.tanh(x[i] * freq_mod) * np.sin(x[i] * freq_mod**2)
        
        # Asymmetric power-law decay with adaptive exponents
        power_term = 0.0
        for i in range(self.dim):
            exponent = 1.6 + 0.4 * np.sin(i * 0.7)
            power_term += (np.abs(x[i]) ** exponent) * np.cos(x[i] * 0.6)
        
        # Global fitness scaling with enhanced complexity
        global_scale = 1.0 + 1.0 * np.exp(-0.12 * np.sum(np.abs(x)))
        
        return global_scale * (0.25 * quantum_term + 0.3 * levy_term + 0.25 * elastic_term + 0.15 * tanh_term + 0.05 * power_term)