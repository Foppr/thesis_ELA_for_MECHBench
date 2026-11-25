import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic parameters for greater complexity
        self.weights = np.random.uniform(1.0, 3.0, dim)
        self.biases = np.random.uniform(-2.0, 2.0, dim)
        self.phase_offsets = np.random.uniform(0, 2*np.pi, dim)
        self.fractal_scales = np.random.uniform(0.5, 1.5, dim)
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired chaotic neural network with phase coupling
        neural_output = 0
        for i in range(self.dim):
            # Phase-modulated quantum weight
            phase_mod = np.sin(x[i] * self.weights[i] + self.phase_offsets[i])
            mod_weight = self.weights[i] * (1 + 0.5 * phase_mod)
            # Quantum activation with superposition
            act = np.tanh(mod_weight * x[i] + self.biases[i]) * np.exp(-0.05 * x[i]**2)
            neural_output += act * np.cos(0.3 * x[i])
        
        # Dynamic fractal topology with quantum scaling
        fractal_term = 0
        for i in range(self.dim):
            scale = self.fractal_scales[i] * (1 + 0.3 * np.sin(x[i] * 3.0 + i * 0.4))
            fractal_term += scale * np.exp(-0.15 * x[i]**2) * np.sin(4.0 * x[i])
        
        # Adaptive gradient modulation with chaotic coupling
        grad_mod = 0
        for i in range(self.dim):
            if i > 0:
                coupling = 0.3 * np.cos(x[i-1] * 1.5 + x[i]) * np.sin(0.7 * x[i])
                grad_mod += coupling
        
        # Multi-scale quantum harmonic interaction
        harmonic_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                freq = 1.0 + 0.5 * np.sin(x[i] + x[j])
                interaction = (x[i]**2 + x[j]**2) * np.cos(freq * (x[i] - x[j]))
                harmonic_interaction += interaction
        
        # Asymmetric quantum multimodal component
        asym_term = 0
        for i in range(self.dim):
            mod_freq = 3.0 + 1.5 * np.sin(x[i] * 0.8 + i * 0.3)
            asym_term += np.sin(mod_freq * x[i]) * np.cos(mod_freq * x[i]**2) * np.exp(-0.08 * x[i]**2)
        
        # Temporal quantum memory effect
        memory_effect = 0
        for i in range(self.dim):
            if i > 1:
                memory = 0.25 * np.sin(x[i-2] + x[i-1] + x[i]) * np.cos(0.6 * x[i])
                memory_effect += memory
        
        # Combine all components with quantum-enhanced weights
        return (0.4 * neural_output + 
                0.3 * fractal_term + 
                0.15 * grad_mod + 
                0.1 * harmonic_interaction + 
                0.05 * asym_term + 
                0.05 * memory_effect)