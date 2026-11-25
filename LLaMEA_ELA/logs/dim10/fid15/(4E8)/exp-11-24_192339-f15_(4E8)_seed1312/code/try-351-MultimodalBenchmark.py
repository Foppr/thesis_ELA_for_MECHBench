import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired superposition states with dynamic phase interference
        superposition = 0
        for i in range(self.dim):
            # Phase modulation with quantum-like tunneling behavior
            phase_mod = np.sin(3.0 * x[i] + 0.7 * np.sin(2.0 * x[i]) * self.dim)
            # Quantum tunneling term with exponential decay
            tunneling = np.exp(-0.2 * x[i]**2) * np.sin(1.5 * x[i])
            superposition += phase_mod * tunneling * (x[i]**2 + 1.0)
        
        # Time-varying chaotic attractor with fractal scaling
        chaotic_attractor = 0
        for i in range(self.dim):
            # Dynamic coupling with time-varying parameters
            dynamic_coupling = 1.0 + 0.5 * np.sin(0.9 * x[i] + 0.3 * np.cos(x[i]) * self.dim)
            # Fractal potential with multi-scale oscillations
            fractal_potential = np.sin(2.0 * x[i] + 0.4 * np.sin(1.2 * x[i])) * \
                               np.cos(1.5 * x[i] + 0.6 * np.cos(x[i]))
            chaotic_attractor += dynamic_coupling * fractal_potential * np.exp(-0.1 * x[i]**2)
        
        # Adaptive ridge structures with quantum energy basins
        ridge_structure = 0
        for i in range(self.dim):
            # Ridge height modulation based on dimensionality
            ridge_height = 2.0 + 1.5 * np.sin(0.8 * x[i] + self.dim * 0.25)
            # Energy basin with adaptive scaling
            energy_basin = np.exp(-0.3 * (x[i]**2)) * np.cos(1.8 * x[i])
            ridge_structure += ridge_height * energy_basin
        
        # Multi-scale oscillatory components with dynamic frequency modulation
        oscillatory = 0
        for i in range(self.dim):
            # Frequency modulation with chaotic behavior
            freq_mod = 3.0 + 2.0 * np.sin(0.5 * x[i] + self.dim * 0.4)
            # Amplitude modulation with adaptive coupling
            amp_mod = 1.0 + 0.8 * np.cos(0.7 * x[i] + self.dim * 0.3)
            oscillatory += freq_mod * amp_mod * np.sin(freq_mod * x[i]) * np.exp(-0.25 * x[i]**2)
        
        # Dynamic coupling with quantum entanglement effects
        entanglement = 0
        for i in range(self.dim):
            for j in range(max(0, i-3), min(i+3, self.dim)):  # Extended coupling range
                # Quantum entanglement strength with dimensionality dependence
                ent_angle = np.sin(1.2 * (x[i] - x[j]) + self.dim * 0.5)
                ent_strength = 0.9 + 0.3 * np.cos(0.8 * (x[i] - x[j]) + self.dim * 0.3)
                entanglement += ent_strength * np.exp(-0.4 * (x[i] - x[j])**2) * \
                              (np.sin(x[i]) * np.cos(x[j]) + ent_angle)
        
        # Fractal dimension scaling with quantum tunneling enhancement
        fractal_dim = 1.5 + 0.4 * np.sin(self.dim * 0.9 + 0.3 * np.cos(x[0] if self.dim > 0 else 0)) + \
                     0.2 * np.sin(4.0 * x[0] if self.dim > 0 else 0) + \
                     0.1 * np.cos(2.0 * x[0] if self.dim > 0 else 0)
        
        # Combined landscape with optimized quantum-enhanced weights
        return (0.35 * superposition + 0.25 * chaotic_attractor + 
                0.2 * ridge_structure + 0.15 * oscillatory + 0.05 * entanglement) * fractal_dim