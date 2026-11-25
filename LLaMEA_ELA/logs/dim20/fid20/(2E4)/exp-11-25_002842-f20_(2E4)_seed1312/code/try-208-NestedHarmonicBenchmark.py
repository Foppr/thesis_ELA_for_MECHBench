import numpy as np

class NestedHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize harmonic oscillator parameters
        self.frequencies = np.random.uniform(1.0, 10.0, dim)
        self.amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.phases = np.random.uniform(0, 2*np.pi, dim)
        self.damping = np.random.uniform(0.1, 1.0, dim)
        # Coupling parameters between dimensions
        self.coupling_strengths = np.random.uniform(0.1, 2.0, (dim, dim))
        self.phase_couplings = np.random.uniform(-0.5, 0.5, (dim, dim))
        # Fractal basin parameters
        self.basin_fractals = np.random.uniform(0.5, 2.0, dim)
        self.basin_shifts = np.random.uniform(-1.0, 1.0, dim)
        # Adaptive frequency modulation parameters
        self.modulation_freq = np.random.uniform(0.1, 1.0, dim)
        self.modulation_amp = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Nested harmonic oscillators with adaptive modulation
        result = 0.0
        for i in range(self.dim):
            # Base harmonic oscillator
            base_osc = self.amplitudes[i] * np.sin(self.frequencies[i] * x_norm[i] + self.phases[i])
            
            # Adaptive frequency modulation
            mod_freq = self.frequencies[i] * (1.0 + self.modulation_amp[i] * np.sin(self.modulation_freq[i] * x_norm[i]))
            mod_osc = self.amplitudes[i] * np.sin(mod_freq * x_norm[i] + self.phases[i])
            
            # Damped oscillation component
            damped_osc = self.amplitudes[i] * np.exp(-self.damping[i] * np.abs(x_norm[i])) * np.cos(self.frequencies[i] * x_norm[i])
            
            # Phase coupling with other dimensions
            phase_coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    phase_coupling += self.coupling_strengths[i, j] * np.sin(
                        self.phase_couplings[i, j] * (x_norm[i] - x_norm[j])
                    )
            
            # Fractal basin boundary effect
            basin_effect = np.exp(-self.basin_fractals[i] * (x_norm[i] - self.basin_shifts[i])**2)
            
            # Combine components with spatial coupling
            result += (base_osc + mod_osc + damped_osc + phase_coupling) * basin_effect
            
        # Spatially coupled harmonic interactions
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Coupled harmonic interaction with distance-dependent weights
                dist = np.abs(x_norm[i] - x_norm[j])
                coupling = self.coupling_strengths[i, j] * np.cos(dist) * np.sin(x_norm[i] + x_norm[j])
                coupling_terms += coupling
                
        # Fractal basin boundary landscape
        basin_landscape = 0.0
        for i in range(self.dim):
            basin_landscape += (np.sin(self.basin_fractals[i] * x_norm[i]) + 
                              0.5 * np.cos(2 * self.basin_fractals[i] * x_norm[i])) * \
                              np.exp(-0.5 * x_norm[i]**2)
            
        # Combine all components
        total = 0.3 * result + 0.4 * coupling_terms + 0.3 * basin_landscape
        
        return total