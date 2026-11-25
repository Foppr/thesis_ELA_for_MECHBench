import numpy as np

class ChaoticQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map chaotic components
        logistic_sum = 0.0
        r = 3.95
        for i in range(self.dim):
            logistic_sum += np.sin(r * x[i] * (1 - x[i])) * np.cos(2 * x[i])
        
        # Quantum harmonic oscillator potential terms
        quantum_potential = 0.0
        for i in range(self.dim):
            quantum_potential += 0.5 * (x[i]**2 + 1.0) * np.sin(3 * x[i]) + 0.3 * x[i]**4
        
        # Adaptive neural network-like interactions
        nn_interaction = 0.0
        for i in range(self.dim):
            activation_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    weight = 1.0 / (1.0 + np.exp(-0.5 * (x[i] - x[j])))
                    activation_sum += weight * np.sin(2 * x[j])
            nn_interaction += activation_sum**2
        
        # Multi-scale fractal-like sine-cosine coupling
        fractal_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale_factor = 1.0 + 0.5 * np.sin(0.1 * (x[i] + x[j]))
                fractal_coupling += scale_factor * np.sin(5 * x[i]) * np.cos(4 * x[j])
        
        # Adaptive parameter modulation with cosine
        adaptive_modulation = 0.0
        for i in range(self.dim):
            param = 1.0 + 0.3 * np.cos(x[i])
            adaptive_modulation += param * (x[i]**3 - 2*x[i]**2 + x[i])
        
        # Boundary penalty with quantum-like tunneling effect
        boundary_penalty = 0.0
        for i in range(self.dim):
            if x[i] < -4.0:
                boundary_penalty += 1.5 * np.exp(-0.5 * (x[i] + 4.0)**2) * np.sin(10 * x[i])
            elif x[i] > 4.0:
                boundary_penalty += 1.2 * np.exp(-0.3 * (x[i] - 4.0)**2) * np.cos(8 * x[i])
        
        # Complex multi-modal structure with exponential coupling
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += np.exp(-0.5 * (x[i] - 1.0)**2) + 0.7 * np.exp(-0.3 * (x[i] + 2.0)**2)
        
        # Phase interference terms with chaotic modulation
        phase_interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_interference += np.sin(3 * x[i]) * np.cos(2 * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Return combined function value
        result = logistic_sum + quantum_potential + nn_interaction + fractal_coupling + \
                 adaptive_modulation + boundary_penalty + multimodal + phase_interference
        
        return result