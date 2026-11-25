import numpy as np

class ChaoticQuantumDefectBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for chaotic resonance wells
        self.resonance_frequencies = np.random.uniform(1.0, 15.0, dim)
        self.resonance_amplitudes = np.random.uniform(0.3, 4.0, dim)
        self.resonance_phases = np.random.uniform(0.0, 2*np.pi, dim)
        # Quantum-like superposition parameters
        self.superposition_weights = np.random.uniform(0.1, 1.5, dim)
        self.superposition_phases = np.random.uniform(0.0, 2*np.pi, dim)
        # Topological defect interaction parameters
        self.defect_strengths = np.random.uniform(0.3, 3.0, dim)
        self.defect_positions = np.random.uniform(-4.5, 4.5, dim)
        self.defect_radii = np.random.uniform(0.05, 1.5, dim)
        # Chaotic modulation parameters
        self.chaotic_parameters = np.random.uniform(0.05, 3.0, dim)
        self.chaotic_feedback = np.random.uniform(0.005, 0.8, (dim, dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Chaotic resonance wells with quantum superposition
        for i in range(self.dim):
            xi = x[i]
            freq = self.resonance_frequencies[i]
            amp = self.resonance_amplitudes[i]
            phase = self.resonance_phases[i]
            
            # Enhanced chaotic resonance term with feedback
            chaotic_term = amp * np.sin(freq * xi + phase)
            for j in range(self.dim):
                if i != j:
                    chaotic_term += self.chaotic_feedback[i][j] * np.sin(freq * x[j] + phase)
                    
            # Enhanced quantum-like superposition
            superposition_term = self.superposition_weights[i] * np.cos(freq * xi + self.superposition_phases[i])
            quantum_effect = 0.3 * (chaotic_term**2 + superposition_term**2) + 0.7 * chaotic_term * superposition_term
            
            result += quantum_effect
            
        # Enhanced topological defect interactions
        for i in range(self.dim):
            xi = x[i]
            defect_strength = self.defect_strengths[i]
            defect_pos = self.defect_positions[i]
            defect_radius = self.defect_radii[i]
            
            # Defect interaction with radial scaling and additional nonlinearity
            distance = np.abs(xi - defect_pos)
            defect_interaction = defect_strength * np.exp(-0.3 * (distance / defect_radius)**2) + 0.1 * np.sin(5 * distance)
            result += defect_interaction
            
        # Enhanced cross-dimensional chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                chaos_strength = self.chaotic_parameters[i] * self.chaotic_parameters[j]
                
                # Enhanced chaotic cross-dimension coupling with multiple frequencies
                chaotic_coupling = chaos_strength * (np.sin(xi - xj) * np.cos(xi + xj) + 0.5 * np.sin(2*(xi - xj)))
                result += chaotic_coupling
                
        # Enhanced quantum interference patterns
        for i in range(self.dim):
            xi = x[i]
            interference = 0.4 * np.sin(2 * xi) * np.cos(3 * xi) + 0.2 * np.sin(5 * xi)
            result += interference
            
        # Enhanced global chaotic modulation with spectral characteristics
        global_chaos = 1.0 + 0.6 * np.sin(np.sum(x) / self.dim) + 0.3 * np.cos(2.0 * np.sum(x))
        global_chaos *= (1.0 + 0.5 * np.cos(3.0 * np.sum(x)) + 0.2 * np.sin(4.0 * np.sum(x)))
        result *= global_chaos
        
        # Enhanced noise to create chaotic behavior
        noise = np.random.normal(0, 0.15, self.dim)
        for i in range(self.dim):
            result += noise[i] * np.sin(self.chaotic_parameters[i] * x[i]) + 0.1 * np.cos(2 * self.chaotic_parameters[i] * x[i])
            
        return result