import numpy as np

class ChaoticQuantumDefectBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for chaotic resonance wells
        self.resonance_frequencies = np.random.uniform(1.0, 8.0, dim)
        self.resonance_amplitudes = np.random.uniform(0.5, 3.0, dim)
        self.resonance_phases = np.random.uniform(0.0, 2*np.pi, dim)
        # Quantum-like superposition parameters
        self.superposition_weights = np.random.uniform(0.1, 1.0, dim)
        self.superposition_phases = np.random.uniform(0.0, 2*np.pi, dim)
        # Topological defect parameters
        self.defect_positions = np.random.uniform(-4.0, 4.0, dim)
        self.defect_strengths = np.random.uniform(1.0, 5.0, dim)
        self.defect_radii = np.random.uniform(0.5, 2.0, dim)
        # Interaction parameters - modified for increased complexity
        self.interaction_strengths = np.random.uniform(0.5, 3.0, (dim, dim))
        # Added chaotic coupling terms for enhanced complexity
        self.chaotic_coupling_strengths = np.random.uniform(0.2, 1.5, (dim, dim))
        
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
            
            # Chaotic resonance term with sinusoidal modulation
            chaotic_term = amp * np.sin(freq * xi + phase) * np.cos(freq * xi + phase)
            # Add quantum-like superposition
            superposition_term = self.superposition_weights[i] * np.sin(2 * xi + self.superposition_phases[i])
            result += chaotic_term + superposition_term
            
        # Topological defect interactions
        for i in range(self.dim):
            xi = x[i]
            position = self.defect_positions[i]
            strength = self.defect_strengths[i]
            radius = self.defect_radii[i]
            
            # Defect interaction with radial scaling
            distance = np.abs(xi - position)
            defect_term = strength * np.exp(-0.5 * (distance / radius)**2)
            result += defect_term
            
        # Cross-dimensional interactions with chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                strength = self.interaction_strengths[i][j]
                
                # Cross-dimension chaotic interaction
                interaction_term = strength * np.sin(xi - xj) * np.cos(xi - xj)
                result += interaction_term
                
                # Add chaotic coupling for enhanced complexity
                chaotic_coupling = self.chaotic_coupling_strengths[i][j] * np.sin(2 * (xi - xj))
                result += chaotic_coupling
                
        # Global chaotic modulation with quantum interference patterns
        global_factor = 1.0 + 0.7 * np.sin(np.sum(x)) * np.cos(np.sum(x))
        global_factor *= (1.0 + 0.4 * np.sin(2.0 * np.sum(x)))
        result *= global_factor
        
        # Add quantum interference terms for complex basin structure
        quantum_interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                interference_term = np.sin(xi + xj) * np.cos(xi - xj)
                quantum_interference += interference_term
                
        result += 0.5 * quantum_interference
        
        return result