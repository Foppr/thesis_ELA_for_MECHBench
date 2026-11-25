import numpy as np

class ChaoticQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Tent map chaotic components with enhanced nonlinearity and multi-scale dynamics
        tent_sum = 0.0
        for i in range(self.dim):
            tent_sum += np.sin(3.14159 * x[i] * (1 - np.abs(x[i]))) * np.cos(2.5 * x[i]) + 0.15 * np.sin(7 * x[i])
        
        # Quantum anharmonic oscillator potential terms with modified coefficients and coupling
        quantum_potential = 0.0
        for i in range(self.dim):
            quantum_potential += 0.4 * (x[i]**2 + 1.5) * np.sin(4 * x[i]) + 0.6 * x[i]**4 + 0.3 * np.cos(5 * x[i]) + 0.1 * x[i]**6
        
        # Deep neural network-like interactions with enhanced coupling and multi-layer structure
        nn_interaction = 0.0
        for i in range(self.dim):
            activation_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    weight = 1.0 / (1.0 + np.exp(-0.5 * (x[i] - x[j])))
                    activation_sum += weight * np.sin(4 * x[j]) * np.cos(x[j]) * np.exp(-0.2 * np.abs(x[j]))
            nn_interaction += activation_sum**3
        
        # Multi-scale fractal-like sine-cosine coupling with increased complexity and dynamic scaling
        fractal_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale_factor = 1.0 + 0.5 * np.sin(0.3 * (x[i] + x[j])) * np.cos(0.2 * (x[i] - x[j]))
                fractal_coupling += scale_factor * np.sin(5 * x[i]) * np.cos(4 * x[j]) + 0.15 * np.sin(7 * x[i] + 3 * x[j])
        
        # Adaptive parameter modulation with enhanced sine coupling and dynamic adjustment
        adaptive_modulation = 0.0
        for i in range(self.dim):
            param = 1.0 + 0.5 * np.cos(x[i]) * np.sin(2 * x[i])
            adaptive_modulation += param * (x[i]**3 - 2*x[i]**2 + x[i]) + 0.2 * np.sin(3 * x[i]) + 0.05 * np.cos(6 * x[i])
        
        # Enhanced boundary penalty with asymmetric tunneling effect and multi-modal penalties
        boundary_penalty = 0.0
        for i in range(self.dim):
            if x[i] < -4.8:
                boundary_penalty += 2.5 * np.exp(-0.35 * (x[i] + 4.8)**2) * np.sin(9 * x[i]) + 0.6 * np.cos(7 * x[i])
            elif x[i] > 4.8:
                boundary_penalty += 2.2 * np.exp(-0.25 * (x[i] - 4.8)**2) * np.cos(8 * x[i]) + 0.4 * np.sin(6 * x[i])
        
        # Enhanced multi-modal structure with additional peaks and complex interactions
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += np.exp(-0.5 * (x[i] - 1.2)**2) + 0.8 * np.exp(-0.3 * (x[i] + 2.2)**2) + 0.5 * np.exp(-0.2 * (x[i] - 3.2)**2) + 0.3 * np.exp(-0.1 * (x[i] + 4.0)**2)
        
        # Enhanced phase interference terms with chaotic modulation and dynamic coupling
        phase_interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_interference += np.sin(5 * x[i]) * np.cos(4 * x[j]) * np.exp(-0.2 * (x[i] - x[j])**2) + 0.25 * np.sin(3 * x[i] + x[j])
        
        # Additional complex harmonic interactions and cross-coupling terms
        harmonic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                harmonic_interaction += 0.1 * np.sin(6 * x[i]) * np.cos(5 * x[j]) * np.exp(-0.1 * (x[i] + x[j])**2) + 0.1 * np.cos(4 * x[i] - 3 * x[j])
        
        # Return combined function value with adjusted weights
        result = tent_sum + quantum_potential + nn_interaction + fractal_coupling + \
                 adaptive_modulation + boundary_penalty + multimodal + phase_interference + harmonic_interaction
        
        return result