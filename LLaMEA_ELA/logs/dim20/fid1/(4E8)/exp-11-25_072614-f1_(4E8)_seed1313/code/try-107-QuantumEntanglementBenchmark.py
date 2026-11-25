import numpy as np

class QuantumEntanglementBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute quantum-like parameters
        self.angles = np.linspace(0, 2*np.pi, min(20, dim))
        self.entanglement_strengths = np.logspace(-1, 1, min(20, dim))
        self.ruggedness_factors = np.linspace(0.5, 2.0, min(20, dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum superposition terms with phase interference
        quantum_terms = []
        for i in range(min(10, self.dim)):
            angle = self.angles[i % len(self.angles)]
            # Superposition of sine and cosine with entangled phases
            term = np.sin(x[i] * angle) * np.cos(x[i] * angle) * \
                   np.exp(-0.5 * (x[i] - np.sin(angle))**2)
            quantum_terms.append(term)
        
        # Entangled variable interactions with adaptive coupling
        entanglement = 0.0
        for i in range(min(self.dim-1, len(self.entanglement_strengths))):
            strength = self.entanglement_strengths[i % len(self.entanglement_strengths)]
            entanglement += strength * np.sin(x[i] + x[i+1]) * np.cos(x[i] - x[i+1])
        
        # Adaptive terrain ruggedness with multi-scale Gaussian hills
        ruggedness = 0.0
        scales = [0.5, 1.0, 2.0]
        for scale in scales:
            for i in range(min(self.dim, len(self.ruggedness_factors))):
                factor = self.ruggedness_factors[i % len(self.ruggedness_factors)]
                ruggedness += factor * np.exp(-((x[i] - scale)**2) / (2 * (scale/3)**2))
        
        # Cross-dimensional interaction terms with quantum tunneling effects
        tunneling = 0.0
        for i in range(min(self.dim-2, len(self.angles))):
            angle = self.angles[i % len(self.angles)]
            tunneling += np.sin(x[i] * x[i+1] * angle) * np.cos(x[i+2] * angle)
        
        # Global structure with polynomial modulation
        global_structure = np.sum(x**4) / (self.dim * 10) + np.sum(np.sin(x)) * 0.5
        
        # Combine all components with dynamic weights based on input magnitude
        input_magnitude = np.mean(np.abs(x))
        weight_quantum = 0.3 * (1 + np.tanh(input_magnitude))
        weight_entanglement = 0.25 * (1 + np.cos(input_magnitude))
        weight_ruggedness = 0.2 * (1 + np.sin(input_magnitude))
        weight_tunneling = 0.15 * (1 + np.tanh(input_magnitude/2))
        weight_global = 0.1
        
        total = (weight_quantum * np.sum(quantum_terms) if quantum_terms else 0 +
                weight_entanglement * entanglement +
                weight_ruggedness * ruggedness +
                weight_tunneling * tunneling +
                weight_global * global_structure)
        
        return total