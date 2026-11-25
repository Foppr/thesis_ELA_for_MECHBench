import numpy as np

class ChaoticQuantumDefectBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for chaotic resonance wells
        self.resonance_frequencies = np.random.uniform(1.0, 10.0, dim)
        self.resonance_amplitudes = np.random.uniform(0.5, 3.0, dim)
        self.resonance_phases = np.random.uniform(0.0, 2*np.pi, dim)
        # Quantum-like superposition parameters
        self.superposition_weights = np.random.uniform(0.1, 1.0, dim)
        self.superposition_phases = np.random.uniform(0.0, 2*np.pi, dim)
        # Topological defect interaction parameters
        self.defect_strengths = np.random.uniform(0.5, 2.5, dim)
        self.defect_positions = np.random.uniform(-4.0, 4.0, dim)
        self.defect_radii = np.random.uniform(0.1, 1.0, dim)
        # Chaotic modulation parameters
        self.chaotic_parameters = np.random.uniform(0.1, 2.0, dim)
        self.chaotic_feedback = np.random.uniform(0.01, 0.5, (dim, dim))
        # Added cubic nonlinearities and modified coupling
        self.cubic_coefficients = np.random.uniform(0.1, 0.5, dim)
        self.modified_coupling = np.random.uniform(0.3, 1.2, (dim, dim))
        
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
            
            # Chaotic resonance term with feedback
            chaotic_term = amp * np.sin(freq * xi + phase)
            for j in range(self.dim):
                if i != j:
                    chaotic_term += self.chaotic_feedback[i][j] * np.sin(freq * x[j] + phase)
                    
            # Quantum-like superposition
            superposition_term = self.superposition_weights[i] * np.cos(freq * xi + self.superposition_phases[i])
            quantum_effect = 0.5 * (chaotic_term**2 + superposition_term**2)
            
            result += quantum_effect
            
        # Topological defect interactions
        for i in range(self.dim):
            xi = x[i]
            defect_strength = self.defect_strengths[i]
            defect_pos = self.defect_positions[i]
            defect_radius = self.defect_radii[i]
            
            # Defect interaction with radial scaling
            distance = np.abs(xi - defect_pos)
            defect_interaction = defect_strength * np.exp(-0.5 * (distance / defect_radius)**2)
            result += defect_interaction
            
        # Cross-dimensional chaotic coupling with modified strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                chaos_strength = self.modified_coupling[i][j] * self.chaotic_parameters[i] * self.chaotic_parameters[j]
                
                # Chaotic cross-dimension coupling with cubic terms
                chaotic_coupling = chaos_strength * np.sin(xi - xj) * np.cos(xi + xj) + 0.1 * (xi**3 - xj**3)
                result += chaotic_coupling
                
        # Adaptive quantum interference patterns with cubic components
        for i in range(self.dim):
            xi = x[i]
            interference = 0.3 * np.sin(2 * xi) * np.cos(3 * xi) + 0.05 * xi**3
            result += interference
            
        # Global chaotic modulation with spectral characteristics
        global_chaos = 1.0 + 0.8 * np.sin(np.sum(x) / self.dim)
        global_chaos *= (1.0 + 0.4 * np.cos(3.0 * np.sum(x)))
        result *= global_chaos
        
        # Add noise to create chaotic behavior
        noise = np.random.normal(0, 0.1, self.dim)
        for i in range(self.dim):
            result += noise[i] * np.sin(self.chaotic_parameters[i] * x[i])
            
        return result