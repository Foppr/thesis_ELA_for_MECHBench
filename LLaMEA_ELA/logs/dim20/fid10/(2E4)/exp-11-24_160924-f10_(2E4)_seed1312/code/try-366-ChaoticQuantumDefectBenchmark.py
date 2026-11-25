import numpy as np

class ChaoticQuantumDefectBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for chaotic resonance wells
        self.resonance_frequencies = np.random.uniform(1.5, 12.0, dim)
        self.resonance_amplitudes = np.random.uniform(0.6, 3.5, dim)
        self.resonance_phases = np.random.uniform(0.0, 2*np.pi, dim)
        # Quantum-like superposition parameters
        self.superposition_weights = np.random.uniform(0.4, 1.3, dim)
        self.superposition_phases = np.random.uniform(0.0, 2*np.pi, dim)
        # Topological defect interaction parameters
        self.defect_strengths = np.random.uniform(1.0, 3.5, dim)
        self.defect_positions = np.random.uniform(-4.0, 4.0, dim)
        self.defect_radii = np.random.uniform(0.3, 1.2, dim)
        # Chaotic modulation parameters
        self.chaotic_parameters = np.random.uniform(0.4, 2.5, dim)
        self.chaotic_feedback = np.random.uniform(0.02, 0.6, (dim, dim))
        # Enhanced noise and interference terms
        self.noise_amplitudes = np.random.uniform(0.05, 0.25, dim)
        self.interference_strengths = np.random.uniform(0.3, 0.8, dim)
        
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
                    
            # Quantum-like superposition with cubic nonlinearity
            superposition_term = self.superposition_weights[i] * np.cos(freq * xi + self.superposition_phases[i])
            quantum_effect = 0.5 * (chaotic_term**2 + superposition_term**2) + 0.15 * chaotic_term**3
            
            result += quantum_effect
            
        # Enhanced topological defect interactions
        for i in range(self.dim):
            xi = x[i]
            defect_strength = self.defect_strengths[i]
            defect_pos = self.defect_positions[i]
            defect_radius = self.defect_radii[i]
            
            # Defect interaction with radial scaling and cubic term
            distance = np.abs(xi - defect_pos)
            defect_interaction = defect_strength * np.exp(-0.5 * (distance / defect_radius)**2) + 0.08 * (distance / defect_radius)**3
            result += defect_interaction
            
        # Cross-dimensional chaotic coupling with cubic terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                chaos_strength = self.chaotic_parameters[i] * self.chaotic_parameters[j]
                
                # Chaotic cross-dimension coupling with cubic interaction
                chaotic_coupling = chaos_strength * np.sin(xi - xj) * np.cos(xi + xj) + 0.12 * (xi - xj)**3
                result += chaotic_coupling
                
        # Adaptive quantum interference patterns with cubic terms
        for i in range(self.dim):
            xi = x[i]
            interference = 0.5 * np.sin(2 * xi) * np.cos(3 * xi) + 0.08 * np.sin(5 * xi)**3
            result += interference
            
        # Global chaotic modulation with enhanced spectral characteristics
        global_chaos = 1.0 + 1.2 * np.sin(np.sum(x) / self.dim)
        global_chaos *= (1.0 + 0.6 * np.cos(3.0 * np.sum(x)) + 0.15 * np.sin(2.0 * np.sum(x))**3)
        result *= global_chaos
        
        # Enhanced noise modulation with improved interference
        for i in range(self.dim):
            noise = self.noise_amplitudes[i] * np.random.normal(0, 0.12)
            interference = self.interference_strengths[i] * np.sin(self.chaotic_parameters[i] * x[i])
            result += noise + 0.05 * x[i]**3 + 0.1 * interference
            
        return result