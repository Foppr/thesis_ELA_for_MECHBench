import numpy as np

class QuantumHarmonicOscillatorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize quantum parameters for each dimension
        self.omega_values = np.random.uniform(0.5, 2.0, dim)
        self.tunneling_strengths = np.random.uniform(0.1, 0.8, dim)
        self.entanglement_angles = np.random.uniform(0, 2*np.pi, dim)
        self.probability_amplitudes = np.random.uniform(0.5, 1.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic oscillator potential
        quantum_potential = 0.0
        for i in range(self.dim):
            omega = self.omega_values[i] * (1.0 + 0.3 * np.sin(0.2 * sum(x)))
            quantum_potential += 0.5 * omega**2 * x[i]**2
            
        # Entangled dimension interactions
        entanglement_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                angle = self.entanglement_angles[i] + self.entanglement_angles[j]
                entanglement_term += np.sin(angle) * np.exp(-0.1 * (x[i] - x[j])**2)
                
        # Probabilistic tunneling effects
        tunneling_term = 0.0
        for i in range(self.dim):
            tunneling_prob = self.tunneling_strengths[i] * np.exp(-0.5 * x[i]**2)
            tunneling_term += tunneling_prob * np.sin(3.0 * x[i])
            
        # Frequency modulation with temporal component
        frequency_modulation = 0.0
        for i in range(self.dim):
            t = sum(x) / self.dim
            mod_freq = self.omega_values[i] * (1.0 + 0.2 * np.cos(0.1 * t))
            frequency_modulation += mod_freq * np.cos(x[i])
            
        # Multi-scale quantum interference
        interference_term = 0.0
        for i in range(self.dim):
            # Multiple interference patterns with different scales
            scales = [0.5, 1.0, 2.0, 4.0]
            for scale in scales:
                interference_term += np.sin(scale * x[i]) * np.cos(scale * x[i] + np.pi/4)
                
        # Boundary tunneling with quantum reflection
        boundary_effect = 0.0
        for i in range(self.dim):
            # Quantum-like behavior near boundaries
            if abs(x[i] + 5.0) < 1.0 or abs(x[i] - 5.0) < 1.0:
                boundary_effect += 2.0 * np.exp(-0.5 * (x[i]**2)) + 0.5 * np.sin(10 * x[i])
                
        # Combine all quantum components with adaptive weights
        result = 0.6 * quantum_potential + 0.4 * entanglement_term + 0.3 * tunneling_term + \
                 0.5 * frequency_modulation + 0.2 * interference_term + 0.1 * boundary_effect
        
        return result