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
            logistic_sum += np.sin(r * x[i] * (1 - x[i])) * np.cos(2 * x[i]) + 0.5 * np.sin(3 * x[i])
        
        # Quantum harmonic oscillator potential terms with dynamic coefficients
        quantum_potential = 0.0
        for i in range(self.dim):
            coeff = 1.0 + 0.2 * np.sin(0.5 * x[i])
            quantum_potential += 0.5 * coeff * (x[i]**2 + 1.0) * np.sin(3 * x[i]) + 0.3 * x[i]**4
        
        # Adaptive neural network-like interactions with dynamic weights
        nn_interaction = 0.0
        for i in range(self.dim):
            activation_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    weight = 1.0 / (1.0 + np.exp(-0.5 * (x[i] - x[j]))) * (1.0 + 0.3 * np.cos(x[i]))
                    activation_sum += weight * np.sin(2 * x[j]) * np.exp(-0.1 * abs(x[i] - x[j]))
            nn_interaction += activation_sum**2
        
        # Multi-scale fractal-like sine-cosine coupling with dynamic scaling
        fractal_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale_factor = 1.0 + 0.5 * np.sin(0.1 * (x[i] + x[j])) * np.cos(0.05 * (x[i] - x[j]))
                fractal_coupling += scale_factor * np.sin(5 * x[i]) * np.cos(4 * x[j]) * np.exp(-0.05 * (x[i] - x[j])**2)
        
        # Adaptive parameter modulation with multi-frequency cosine
        adaptive_modulation = 0.0
        for i in range(self.dim):
            param = 1.0 + 0.3 * np.cos(x[i]) + 0.2 * np.sin(2 * x[i])
            adaptive_modulation += param * (x[i]**3 - 2*x[i]**2 + x[i]) * np.exp(-0.1 * abs(x[i]))
        
        # Enhanced boundary penalty with quantum-like tunneling effect
        boundary_penalty = 0.0
        for i in range(self.dim):
            if x[i] < -4.0:
                boundary_penalty += 1.5 * np.exp(-0.5 * (x[i] + 4.0)**2) * np.sin(10 * x[i]) * (1.0 + 0.1 * np.cos(5 * x[i]))
            elif x[i] > 4.0:
                boundary_penalty += 1.2 * np.exp(-0.3 * (x[i] - 4.0)**2) * np.cos(8 * x[i]) * (1.0 + 0.1 * np.sin(4 * x[i]))
        
        # Complex multi-modal structure with exponential coupling and phase shifts
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += np.exp(-0.5 * (x[i] - 1.0)**2) + 0.7 * np.exp(-0.3 * (x[i] + 2.0)**2) + 0.3 * np.sin(3 * x[i])
        
        # Phase interference terms with chaotic modulation and dynamic coupling
        phase_interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 1.0 + 0.2 * np.sin(0.5 * (x[i] + x[j]))
                phase_interference += coupling_strength * np.sin(3 * x[i]) * np.cos(2 * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2) * np.cos(0.1 * (x[i] + x[j]))
        
        # Additional chaotic coupling terms for increased complexity
        chaotic_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_term = np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.2 * (x[i] - x[j])**2)
                chaotic_coupling += chaotic_term * (1.0 + 0.1 * np.sin(5 * x[i]))
        
        # Return combined function value
        result = logistic_sum + quantum_potential + nn_interaction + fractal_coupling + \
                 adaptive_modulation + boundary_penalty + multimodal + phase_interference + chaotic_coupling
        
        return result