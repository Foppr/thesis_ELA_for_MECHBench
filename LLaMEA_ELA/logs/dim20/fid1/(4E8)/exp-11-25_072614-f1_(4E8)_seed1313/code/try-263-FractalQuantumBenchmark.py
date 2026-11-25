import numpy as np

class FractalQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal sequence for dimension-specific scaling
        self.fractal_seq = np.array([1.0, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0.0078125, 0.00390625, 0.001953125])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-based scaling with quantum harmonic oscillator components
        fractal_term = 0.0
        for i in range(self.dim):
            # Fractal scaling factor based on dimension index
            scale_factor = self.fractal_seq[i % len(self.fractal_seq)]
            # Quantum harmonic oscillator potential: V(x) = 0.5 * omega^2 * x^2
            omega = 1.0 + 0.5 * np.sin(0.3 * np.pi * i)
            fractal_term += scale_factor * 0.5 * omega**2 * x[i]**2
        fractal_term /= self.dim
        
        # Quantum harmonic oscillator with temporal coupling
        quantum_term = 0.0
        for i in range(self.dim):
            omega = 1.5 + 0.3 * np.cos(0.4 * np.pi * i)
            quantum_term += 0.5 * omega**2 * x[i]**2 * np.exp(-0.1 * x[i]**2)
        quantum_term /= self.dim
        
        # Temporal coupling with chaotic phase modulation
        temporal_term = 0.0
        for i in range(self.dim):
            phase = 0.2 * np.sin(0.5 * np.pi * i + 0.3 * np.sum(x))
            temporal_term += np.sin(x[i] + phase) * np.exp(-0.05 * x[i]**2)
        temporal_term /= self.dim
        
        # Modified interaction terms with enhanced cross-dimensional coupling
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.3 + 0.7 * np.sin(0.2 * (i - j) + 0.5 * np.sum(x))
                interaction_term += coupling_strength * np.exp(-0.2 * (x[i] - x[j])**2) * np.cos(0.6 * (x[i] + x[j]))
        interaction_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Enhanced cross-dimensional coupling with fractal modulation
        cross_coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale_factor = self.fractal_seq[(i + j) % len(self.fractal_seq)]
                cross_coupling_term += scale_factor * np.exp(-0.15 * (x[i] - x[j])**2) * np.sin(0.8 * (x[i] + x[j]))
        cross_coupling_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Fractal-based multimodal structure with quantum interference
        modal_term = 0.0
        for i in range(self.dim):
            scale_factor = self.fractal_seq[i % len(self.fractal_seq)]
            modal_term += scale_factor * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]) * np.exp(-0.1 * x[i]**2)
        modal_term /= self.dim
        
        # Quantum tunneling effect with adaptive barrier heights
        tunneling_term = 0.0
        for i in range(self.dim):
            barrier_height = 1.0 + 0.4 * np.cos(0.6 * np.pi * i)
            tunneling_term += barrier_height * np.exp(-0.5 * (x[i] / 0.8)**2) * np.sin(0.7 * x[i])
        tunneling_term /= self.dim
        
        # Multi-scale ridge with fractal modulation
        ridge_term = 0.0
        for i in range(self.dim):
            mod_factor = 1.0 + 0.3 * np.sin(0.4 * np.pi * i)
            ridge_term += mod_factor * np.cos(x[i]) * np.exp(-0.08 * x[i]**2)
        ridge_term /= self.dim
        
        # Multi-scale interaction with quantum coupling
        quantum_interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_factor = 0.5 + 0.5 * np.cos(0.3 * (i - j) + 0.4 * np.sum(x))
                quantum_interaction_term += coupling_factor * np.exp(-0.1 * (x[i] - x[j])**2) * np.tan(0.5 * (x[i] + x[j]))
        quantum_interaction_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Combine all terms with dynamic weights based on fractal sequence
        weights = self.fractal_seq[:self.dim]
        weights = weights / np.sum(weights)
        
        total = (weights[0] * fractal_term + 
                 weights[1] * quantum_term + 
                 weights[2] * temporal_term + 
                 weights[3] * interaction_term + 
                 weights[4] * cross_coupling_term + 
                 weights[5] * modal_term + 
                 weights[6] * tunneling_term + 
                 weights[7] * ridge_term + 
                 weights[8] * quantum_interaction_term)
        
        return total