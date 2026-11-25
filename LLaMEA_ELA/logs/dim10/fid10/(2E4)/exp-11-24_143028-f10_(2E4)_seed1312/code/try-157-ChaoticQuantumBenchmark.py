import numpy as np

class ChaoticQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map chaotic components with enhanced nonlinearity
        logistic_sum = 0.0
        r = 3.99
        for i in range(self.dim):
            logistic_sum += np.sin(r * x[i] * (1 - x[i])) * np.cos(2 * x[i]) + 0.1 * np.sin(5 * x[i])
        
        # Quantum harmonic oscillator potential terms with modified coefficients
        quantum_potential = 0.0
        for i in range(self.dim):
            quantum_potential += 0.3 * (x[i]**2 + 1.0) * np.sin(3 * x[i]) + 0.5 * x[i]**4 + 0.2 * np.cos(4 * x[i])
        
        # Adaptive neural network-like interactions with enhanced coupling
        nn_interaction = 0.0
        for i in range(self.dim):
            activation_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    weight = 1.0 / (1.0 + np.exp(-0.3 * (x[i] - x[j])))
                    activation_sum += weight * np.sin(3 * x[j]) * np.cos(x[j])
            nn_interaction += activation_sum**2
        
        # Multi-scale fractal-like sine-cosine coupling with increased complexity
        fractal_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale_factor = 1.0 + 0.3 * np.sin(0.2 * (x[i] + x[j]))
                fractal_coupling += scale_factor * np.sin(4 * x[i]) * np.cos(3 * x[j]) + 0.1 * np.sin(6 * x[i] + 2 * x[j])
        
        # Adaptive parameter modulation with enhanced sine coupling
        adaptive_modulation = 0.0
        for i in range(self.dim):
            param = 1.0 + 0.4 * np.cos(x[i])
            adaptive_modulation += param * (x[i]**3 - 2*x[i]**2 + x[i]) + 0.15 * np.sin(2 * x[i])
        
        # Enhanced boundary penalty with asymmetric tunneling effect
        boundary_penalty = 0.0
        for i in range(self.dim):
            if x[i] < -4.5:
                boundary_penalty += 2.0 * np.exp(-0.3 * (x[i] + 4.5)**2) * np.sin(8 * x[i]) + 0.5 * np.cos(6 * x[i])
            elif x[i] > 4.5:
                boundary_penalty += 1.8 * np.exp(-0.2 * (x[i] - 4.5)**2) * np.cos(7 * x[i]) + 0.3 * np.sin(5 * x[i])
        
        # Enhanced multi-modal structure with additional peaks
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += np.exp(-0.5 * (x[i] - 1.0)**2) + 0.7 * np.exp(-0.3 * (x[i] + 2.0)**2) + 0.4 * np.exp(-0.2 * (x[i] - 3.0)**2)
        
        # Enhanced phase interference terms with chaotic modulation
        phase_interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_interference += np.sin(4 * x[i]) * np.cos(3 * x[j]) * np.exp(-0.15 * (x[i] - x[j])**2) + 0.2 * np.sin(2 * x[i] + x[j])
        
        # Return combined function value with adjusted weights
        result = logistic_sum + quantum_potential + nn_interaction + fractal_coupling + \
                 adaptive_modulation + boundary_penalty + multimodal + phase_interference
        
        return result