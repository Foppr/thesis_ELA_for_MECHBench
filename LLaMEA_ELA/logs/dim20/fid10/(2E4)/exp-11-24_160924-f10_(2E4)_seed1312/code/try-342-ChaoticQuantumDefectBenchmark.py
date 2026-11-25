import numpy as np

class ChaoticQuantumDefectBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize hyper-chaotic system parameters
        self.hyperchaos_params = np.random.uniform(0.5, 1.5, dim)
        self.quantum_entanglement_phases = np.random.uniform(0, 2*np.pi, dim)
        self.defect_strengths = np.random.uniform(1.0, 3.0, dim)
        self.defect_positions = np.random.uniform(-4.5, 4.5, dim)
        self.resonance_gains = np.random.uniform(0.5, 2.0, dim)
        self.entanglement_weights = np.random.uniform(0.2, 0.8, dim)
        self.topological_charges = np.random.choice([-2, -1, 1, 2], dim)
        self.interaction_couplings = np.random.uniform(0.2, 1.5, (dim, dim))
        self.quantum_damping = np.random.uniform(0.02, 0.3, dim)
        self.classical_friction = np.random.uniform(0.1, 0.6, dim)
        self.energy_scales = np.random.uniform(0.5, 6.0, dim)
        self.fractal_scaling = np.random.uniform(0.1, 2.0, dim)
        self.adaptive_noise = np.random.uniform(0.01, 0.2, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Hyper-chaotic resonance components with quantum entanglement
        for i in range(self.dim):
            xi = x[i]
            hyperchaos_param = self.hyperchaos_params[i]
            phase = self.quantum_entanglement_phases[i]
            
            # Hyper-chaotic logistic map with multiple frequencies and quantum phases
            chaotic_term = np.sin(phase + hyperchaos_param * xi)
            chaotic_term += 0.7 * np.sin(2 * phase + 2 * hyperchaos_param * xi)
            chaotic_term += 0.5 * np.sin(3 * phase + 3 * hyperchaos_param * xi)
            chaotic_term += 0.3 * np.sin(4 * phase + 4 * hyperchaos_param * xi)
            
            # Quantum entanglement superposition with weighting
            entanglement = self.entanglement_weights[i] * chaotic_term
            result += entanglement
            
        # Topological defect interactions with fractal energy scaling
        for i in range(self.dim):
            xi = x[i]
            defect_pos = self.defect_positions[i]
            defect_strength = self.defect_strengths[i]
            charge = self.topological_charges[i]
            fractal_scale = self.fractal_scaling[i]
            
            # Defect interaction with fractal scaling and topological charge
            distance = np.abs(xi - defect_pos)
            defect_term = defect_strength * np.exp(-distance**2 / (2 * fractal_scale**2)) * charge
            result += defect_term
            
        # Quantum harmonic oscillator with hyper-resonance and adaptive noise
        for i in range(self.dim):
            xi = x[i]
            gain = self.resonance_gains[i]
            energy_scale = self.energy_scales[i]
            noise = self.adaptive_noise[i]
            
            # Hyper-quantum harmonic oscillator with resonance gain and noise modulation
            quantum_harmonic = 0.5 * energy_scale * xi**2 + gain * np.sin(xi)
            quantum_harmonic += 0.4 * energy_scale * np.sin(2 * xi)
            quantum_harmonic += 0.2 * energy_scale * np.sin(3 * xi)
            quantum_harmonic += noise * np.random.normal(0, 1)
            result += quantum_harmonic
            
        # Cross-dimensional quantum entanglement with classical friction and fractal coupling
        for i in range(self.dim):
            xi = x[i]
            damping = self.quantum_damping[i]
            friction = self.classical_friction[i]
            fractal_scale = self.fractal_scaling[i]
            
            # Quantum damping with classical friction coupling and fractal influence
            damping_term = damping * np.exp(-xi**2 / (2 * fractal_scale)) + friction * xi**2
            result += damping_term
            
        # Multi-scale interaction terms with fractal-like coupling and quantum entanglement
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                coupling = self.interaction_couplings[i][j]
                
                # Quantum entanglement-like interaction with fractal scaling and topological influence
                interaction = coupling * np.sin(xi + xj) * np.cos(xi - xj)
                interaction += 0.6 * coupling * np.sin(2*(xi + xj)) * np.cos(2*(xi - xj))
                interaction += 0.4 * coupling * np.sin(3*(xi + xj)) * np.cos(3*(xi - xj))
                result += interaction
                
        # Global quantum phase modulation with hyper-chaos and fractal influence
        global_phase = np.sum(self.quantum_entanglement_phases) / self.dim
        hyperchaotic_modulation = np.sin(global_phase + np.sum(x)) * np.cos(np.sum(x**2))
        result *= (1.0 + 0.4 * hyperchaotic_modulation)
        
        # Fractal energy scaling factor for complex landscape structure
        fractal_factor = np.prod(np.power(self.fractal_scaling, 1.0/self.dim))
        result *= fractal_factor
        
        return result