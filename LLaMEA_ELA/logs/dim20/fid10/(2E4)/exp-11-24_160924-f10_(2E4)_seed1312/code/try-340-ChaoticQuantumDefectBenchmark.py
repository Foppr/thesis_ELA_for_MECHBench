import numpy as np

class ChaoticQuantumDefectBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize chaotic system parameters
        self.chaotic_params = np.random.uniform(0.1, 0.9, dim)
        self.quantum_phases = np.random.uniform(0, 2*np.pi, dim)
        self.defect_strengths = np.random.uniform(0.5, 2.5, dim)
        self.defect_positions = np.random.uniform(-4.0, 4.0, dim)
        self.resonance_gains = np.random.uniform(0.3, 1.7, dim)
        self.superposition_weights = np.random.uniform(0.1, 0.9, dim)
        self.topological_charges = np.random.choice([-1, 1], dim)
        self.interaction_couplings = np.random.uniform(0.1, 1.0, (dim, dim))
        self.quantum_damping = np.random.uniform(0.01, 0.2, dim)
        self.classical_friction = np.random.uniform(0.05, 0.5, dim)
        self.energy_scales = np.random.uniform(1.0, 5.0, dim)
        # Fractal and memory components
        self.fractal_dimensions = np.random.uniform(1.1, 2.9, dim)
        self.memory_weights = np.random.uniform(0.05, 0.3, dim)
        self.historical_influences = np.random.uniform(-0.5, 0.5, (dim, 3))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Chaotic resonance components with quantum-like behavior
        for i in range(self.dim):
            xi = x[i]
            chaotic_param = self.chaotic_params[i]
            phase = self.quantum_phases[i]
            
            # Logistic map-inspired chaotic term with quantum phase modulation
            chaotic_term = np.sin(phase + chaotic_param * xi)
            chaotic_term += 0.5 * np.sin(2 * phase + 2 * chaotic_param * xi)
            chaotic_term += 0.3 * np.sin(3 * phase + 3 * chaotic_param * xi)
            
            # Quantum-like superposition with weighting
            superposition = self.superposition_weights[i] * chaotic_term
            result += superposition
            
        # Topological defect interactions with quantum characteristics
        for i in range(self.dim):
            xi = x[i]
            defect_pos = self.defect_positions[i]
            defect_strength = self.defect_strengths[i]
            charge = self.topological_charges[i]
            
            # Defect interaction with exponential decay and topological charge
            distance = np.abs(xi - defect_pos)
            defect_term = defect_strength * np.exp(-distance**2 / (2 * 0.5**2)) * charge
            result += defect_term
            
        # Quantum harmonic oscillator components with resonance
        for i in range(self.dim):
            xi = x[i]
            gain = self.resonance_gains[i]
            energy_scale = self.energy_scales[i]
            
            # Quantum-like harmonic oscillator with resonance gain
            quantum_harmonic = 0.5 * energy_scale * xi**2 + gain * np.sin(xi)
            quantum_harmonic += 0.3 * energy_scale * np.sin(2 * xi)
            result += quantum_harmonic
            
        # Cross-dimensional quantum entanglement and classical friction
        for i in range(self.dim):
            xi = x[i]
            damping = self.quantum_damping[i]
            friction = self.classical_friction[i]
            
            # Quantum damping with classical friction coupling
            damping_term = damping * np.exp(-xi**2 / 2) + friction * xi**2
            result += damping_term
            
        # Multi-scale interaction terms with fractal-like coupling
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                coupling = self.interaction_couplings[i][j]
                
                # Quantum entanglement-like interaction with topological defect influence
                interaction = coupling * np.sin(xi + xj) * np.cos(xi - xj)
                interaction += 0.5 * coupling * np.sin(2*(xi + xj)) * np.cos(2*(xi - xj))
                result += interaction
                
        # Global quantum phase modulation with classical chaos
        global_phase = np.sum(self.quantum_phases) / self.dim
        chaotic_modulation = np.sin(global_phase + np.sum(x))
        result *= (1.0 + 0.3 * chaotic_modulation)
        
        # Fractal geometry influence
        for i in range(self.dim):
            xi = x[i]
            fractal_dim = self.fractal_dimensions[i]
            result += 0.2 * np.sin(xi**fractal_dim) * np.cos(xi**(fractal_dim/2))
            
        # Memory-dependent dynamics
        for i in range(self.dim):
            if i > 0:
                historical_influence = np.sum(self.historical_influences[i] * x[max(0, i-3):i])
                result += self.memory_weights[i] * historical_influence
                
        return result